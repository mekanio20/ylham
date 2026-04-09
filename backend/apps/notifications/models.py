from django.db import models
from django.conf import settings


class Notification(models.Model):

    NOTIFICATION_TYPES = [
        ('like', 'Beğeni'),
        ('comment', 'Yorum'),
        ('follower', 'Takipçi'),
        ('system', 'Sistem'),
    ]

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name='Alıcı'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sent_notifications',
        verbose_name='Gönderen'
    )
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        verbose_name='Bildirim Türü'
    )
    poem = models.ForeignKey(
        'poems.Poem',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications',
        verbose_name='İlgili Şiir'
    )
    message = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Mesaj',
        help_text='Sistem bildirimleri için özel mesaj'
    )
    is_read = models.BooleanField(default=False, verbose_name='Okundu mu')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Bildirim'
        verbose_name_plural = 'Bildirimler'
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.get_notification_type_display()}] → {self.recipient.username}'

    def get_message(self):
        """Bildirim türüne göre otomatik mesaj üretir."""
        if self.notification_type == 'like' and self.sender and self.poem:
            return f'{self.sender.username} şiirinizi beğendi: "{self.poem.title}"'
        elif self.notification_type == 'comment' and self.sender and self.poem:
            return f'{self.sender.username} şiirinize yorum yaptı: "{self.poem.title}"'
        elif self.notification_type == 'follower' and self.sender:
            return f'{self.sender.username} sizi takip etmeye başladı.'
        elif self.notification_type == 'system':
            return self.message or 'Yeni bir sistem bildirimi var.'
        return 'Yeni bir bildiriminiz var.'