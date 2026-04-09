from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class Poem(models.Model):

    MUSIC_CHOICES = settings.POEM_BACKGROUND_MUSIC_CHOICES
    BACKGROUND_IMAGE_CHOICES = settings.POEM_BACKGROUND_IMAGE_CHOICES
    PUBLIC_STATUS_CHOICES = [
        ('public', 'Public'),
        ('followers', 'Followers'),
        ('private', 'Private'),
    ]

    # ── Temel alanlar ────────────────────────────────────────────────────────
    title = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2)],
        verbose_name='Ady'
    )
    content = models.TextField(
        validators=[MinLengthValidator(20)],
        verbose_name='Goşgy'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='poems',
        verbose_name='Ýazyjy'
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='poems',
        verbose_name='Kategoriýa'
    )
    tags = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='Taglar',
        help_text='Oty belgisi bilen taglary girizip bolýar: söýgi, tebigat, ýalňyzlyk'
    )

    # ── Medya ────────────────────────────────────────────────────────────────
    background_image = models.CharField(
        max_length=50,
        choices=BACKGROUND_IMAGE_CHOICES,
        default='none',
        verbose_name='Arka fon suraty'
    )
    background_music = models.CharField(
        max_length=20,
        choices=MUSIC_CHOICES,
        default='none',
        verbose_name='Arka fon sazy'
    )

    # ── Sayaçlar (denormalize — performans için) ─────────────────────────────
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)

    # ── Durum ────────────────────────────────────────────────────────────────
    is_draft = models.BooleanField(default=False, verbose_name='Garalama')
    public_status = models.CharField(
        max_length=20,
        choices=PUBLIC_STATUS_CHOICES,
        default='public',
        verbose_name='Kimler görmeli'
    )
    poem_note = models.TextField(
        blank=True,
        default='',
        verbose_name='Şahyryň belligi'
    )
    comment_permission = models.BooleanField(
        default=True,
        verbose_name='Teswir rugsady'
    )
    approve = models.BooleanField(
        default=False,
        verbose_name='Admin tassyklamasy',
        help_text='Tassyklanmasa, diňe ýazyjy we admin görýär; beýleki ulanyjylar üçin görünmeýär.',
    )
    is_deleted = models.BooleanField(default=False, verbose_name='Pozuldy')
    deleted_at = models.DateTimeField(null=True, blank=True)

    # ── Zaman ────────────────────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'poems'
        verbose_name = 'Goşgy'
        verbose_name_plural = 'Goşgular'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} — {self.author.username}'

    def is_visible_to(self, user):
        """Beýleki ulanyjylar üçin diňe tassyklanan, ýaýda ýagdaýdaky goşgylar."""
        if self.is_deleted:
            return False
        if user.is_authenticated:
            if getattr(user, 'is_staff', False):
                return True
            if self.author_id == user.id:
                return True
        if self.is_draft:
            return False
        if not self.approve:
            return False
        return True

    def get_tags_list(self):
        """Tag stringden liste öwür."""
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def set_tags_from_list(self, tags: list):
        """List formatdaky taglari stringe öwürýär."""
        self.tags = ', '.join([t.strip() for t in tags if t.strip()])


class PoemView(models.Model):
    """
    Görüntülenme tekrarını engellemek için kullanılır.
    Giriş yapmış kullanıcı → (poem, user) unique
    Anonim kullanıcı       → (poem, ip_address) unique (yaklaşık)
    """
    poem = models.ForeignKey(
        Poem,
        on_delete=models.CASCADE,
        related_name='views',
        verbose_name='Goşgy'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='poem_views',
        verbose_name='Ulanyjy'
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name='IP Adresi'
    )
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'poem_views'
        verbose_name = 'Okalma sany'
        verbose_name_plural = 'Okalanlar sany'
        constraints = [
            models.UniqueConstraint(
                fields=['poem', 'user'],
                condition=models.Q(user__isnull=False),
                name='unique_poem_user_view'
            ),
            models.UniqueConstraint(
                fields=['poem', 'ip_address'],
                condition=models.Q(user__isnull=True),
                name='unique_poem_ip_view'
            ),
        ]

    def __str__(self):
        who = self.user.username if self.user else self.ip_address
        return f'{self.poem.title} ← {who}'