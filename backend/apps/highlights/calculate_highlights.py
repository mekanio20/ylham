"""
python manage.py calculate_highlights

Otomatik highlight hesaplama komutu.
Cron job ile periyodik çalıştırılır:

  # Her gece gece yarısı daily highlights hesapla
  0 0 * * * /path/to/venv/bin/python manage.py calculate_highlights --period=daily

  # Her Pazartesi weekly
  0 0 * * 1 /path/to/venv/bin/python manage.py calculate_highlights --period=weekly

  # Her ayın 1'inde monthly
  0 0 1 * * /path/to/venv/bin/python manage.py calculate_highlights --period=monthly

  # Her yılın 1 Ocak'ında yearly
  0 0 1 1 * /path/to/venv/bin/python manage.py calculate_highlights --period=yearly
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from apps.highlights.models import Highlight
from apps.poems.models import Poem


class Command(BaseCommand):
    help = 'Belirtilen periyot için en iyi şiirleri hesaplar ve highlight olarak kaydeder.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--period',
            type=str,
            default='daily',
            choices=['daily', 'weekly', 'monthly', 'yearly'],
            help='Hesaplanacak periyot (varsayılan: daily)'
        )
        parser.add_argument(
            '--top',
            type=int,
            default=10,
            help='Kaç şiir seçilsin (varsayılan: 10)'
        )

    def handle(self, *args, **options):
        period = options['period']
        top_n = options['top']
        now = timezone.now()

        # Periyoda göre tarih filtresi
        date_filter = {
            'daily':   now - timedelta(days=1),
            'weekly':  now - timedelta(weeks=1),
            'monthly': now - timedelta(days=30),
            'yearly':  now - timedelta(days=365),
        }
        since = date_filter[period]

        # Skor formülü: view_count + (like_count * 3)
        # Manuel seçilmiş olanları ATLAMA — onları koruyoruz
        manual_ranks = set(
            Highlight.objects.filter(period=period, is_manual=True)
            .values_list('rank', flat=True)
        )

        # En iyi şiirleri çek (yasaklı ve silinmiş hariç)
        poems = Poem.objects.filter(
            is_deleted=False,
            is_draft=False,
            approve=True,
            author__is_banned=False,
            created_at__gte=since,
        ).order_by(
            # En yüksek skor önce
        )

        # Skoru Python tarafında hesapla ve sırala
        scored = []
        for poem in poems:
            score = poem.view_count + (poem.like_count * 3)
            scored.append((score, poem))

        scored.sort(key=lambda x: x[0], reverse=True)

        # Manuel olmayan rank slotlarını doldur
        available_ranks = [r for r in range(1, 11) if r not in manual_ranks]
        saved = 0

        for rank, (score, poem) in zip(available_ranks, scored[:top_n]):
            Highlight.objects.update_or_create(
                period=period,
                rank=rank,
                defaults={
                    'poem': poem,
                    'score': score,
                    'is_manual': False,
                    'selected_by': None,
                }
            )
            saved += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'[{period.upper()}] {saved} highlight güncellendi. '
                f'({len(manual_ranks)} manuel slot korundu)'
            )
        )