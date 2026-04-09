from django.db import models
from django.conf import settings


class Highlight(models.Model):

    PERIOD_CHOICES = [
        ('daily', 'Günlük'),
        ('weekly', 'Haftalık'),
        ('monthly', 'Aylık'),
        ('yearly', 'Yıllık'),
    ]

    poem = models.ForeignKey(
        'poems.Poem',
        on_delete=models.CASCADE,
        related_name='highlights',
        verbose_name='Şiir'
    )
    period = models.CharField(
        max_length=10,
        choices=PERIOD_CHOICES,
        default='daily',
        verbose_name='Periyot'
    )
    rank = models.PositiveSmallIntegerField(
        verbose_name='Sıralama',
        help_text='1 ile 10 arasında olmalıdır'
    )
    score = models.FloatField(
        default=0.0,
        verbose_name='Hesaplanan Skor',
        help_text='view_count + (like_count * 3) formülü ile hesaplanır'
    )
    is_manual = models.BooleanField(
        default=False,
        verbose_name='Manuel Seçim',
        help_text='Admin tarafından manuel seçildiyse True'
    )
    selected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='highlights_selected',
        verbose_name='Seçen Admin'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'highlights'
        verbose_name = 'Öne Çıkan'
        verbose_name_plural = 'Öne Çıkanlar'
        # Aynı periyotta aynı rank bir kez olabilir
        unique_together = ('period', 'rank')
        ordering = ['period', 'rank']

    def __str__(self):
        return f'[{self.get_period_display()}] #{self.rank} - {self.poem.title}'

    def clean(self):
        from django.core.exceptions import ValidationError
        if not (1 <= self.rank <= 10):
            raise ValidationError({'rank': 'Sıralama 1 ile 10 arasında olmalıdır.'})