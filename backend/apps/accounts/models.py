from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from datetime import timedelta
import random
import string

class PasswordResetOTP(models.Model):
    """
    Açar sözü täzelenmek üçin OTP ýazgy.
    Her bir elektron poçta üçin diňe bir işjeň ýazgy saklanýar.
    """
    email = models.EmailField()
    code = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = "Password Reset OTP"
        indexes = [
            models.Index(fields=['email', 'is_used']),
        ]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expires_at = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    @staticmethod
    def generate_code():
        return ''.join(random.choices(string.digits, k=6))

class EmailVerification(models.Model):
    """
    Ýazgydan öň elektron poçta tassyklaýyş üçin wagtlaýyn ýazgy.
    Ulanyjy heniz döredilmeýär; tassyklaýyş tamamlanandan soň dörediler.
    """
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)  # make_password ile hash'lenmiş
    code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)  # yanlış deneme sayısı
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = "Email Verification"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expires_at = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    @staticmethod
    def generate_code():
        return ''.join(random.choices(string.digits, k=6))


# ─── CUSTOM USER MANAGER ──────────────────────────────────────────────────────

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email required.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)


# ─── USER MODEL ───────────────────────────────────────────────────────────────

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={'unique': 'This username is already taken.'},
        default=''.join(random.choices(string.digits, k=14))
    )
    email = models.EmailField(
        unique=True,
        error_messages={'unique': 'This email is already taken.'}
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

    # Brute force koruması
    failed_login_attempts = models.PositiveIntegerField(default=0)
    lockout_until = models.DateTimeField(null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'

    def __str__(self):
        return self.username

    def is_locked_out(self):
        """Hesap kilitli mi kontrol eder."""
        if self.lockout_until and timezone.now() < self.lockout_until:
            return True
        return False

    def increment_failed_login(self):
        """Başarısız giriş sayacını artırır, gerekirse kilitler."""
        from django.conf import settings
        max_attempts = getattr(settings, 'LOGIN_MAX_ATTEMPTS', 10)
        lockout_minutes = getattr(settings, 'LOGIN_LOCKOUT_MINUTES', 1)

        self.failed_login_attempts += 1

        if self.failed_login_attempts >= max_attempts:
            self.lockout_until = timezone.now() + timezone.timedelta(minutes=lockout_minutes)

        self.save(update_fields=['failed_login_attempts', 'lockout_until'])

    def reset_failed_login(self):
        """Başarılı girişte sayacı sıfırlar."""
        if self.failed_login_attempts > 0 or self.lockout_until:
            self.failed_login_attempts = 0
            self.lockout_until = None
            self.save(update_fields=['failed_login_attempts', 'lockout_until'])


# ─── POET PROFILE ─────────────────────────────────────────────────────────────

class PoetProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='poet_profile'
    )
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    instagram = models.CharField(max_length=100, blank=True, default='')
    tiktok = models.CharField(max_length=100, blank=True, default='')
    imo = models.CharField(max_length=100, blank=True, default='')
    bio = models.TextField(max_length=500, blank=True, default='')
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        default='/poet_images/default.webp',
        blank=True
    )
    avatar_thumbnail = models.ImageField(
        upload_to='avatars/thumbnails/',
        null=True,
        blank=True
    )
    total_score = models.IntegerField(default=0)
    is_private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'poet_profiles'
        verbose_name = 'Şahyr Profili'
        verbose_name_plural = 'Şahry Profilleri'

    def __str__(self):
        return f'{self.user.username} - Profil'

    @property
    def poem_count(self):
        return self.user.poems.filter(
            is_deleted=False, is_draft=False, approve=True
        ).count()