from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import User, PoetProfile, EmailVerification, PasswordResetOTP
from core.utils import validate_image_file
from datetime import timedelta

class ForgotPasswordRequestSerializer(serializers.Serializer):
    """
    1-nji ädim: Elektron poçta alyň, OTP iberiň.
    Howpsuzlyk üçin, elektron poçta ulgamyň içinde ýok bolsa-da, üstünlikli jogap berilýär
    (ulanyjy sanamak hüjüminden goraýyş üçin).
    """
    email = serializers.EmailField()

    def validate_email(self, value):
        return value.lower().strip()


class ForgotPasswordVerifySerializer(serializers.Serializer):
    """
    2-nji ädim: OTP we täze açar sözü alyň, tassyklaň we açar sözü täzeläň.
    """
    email = serializers.EmailField()
    code = serializers.CharField(min_length=6, max_length=6)
    new_password = serializers.CharField(min_length=8, write_only=True)
    new_password_confirm = serializers.CharField(min_length=8, write_only=True)

    def validate(self, attrs):
        # Şifre eşleşme kontrolü
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError(
                {"new_password_confirm": "Açar sözler gabat gelmeýär."}
            )

        email = attrs['email'].lower().strip()

        # Aktif OTP kaydını bul
        try:
            otp = PasswordResetOTP.objects.filter(
                email=email,
                is_used=False,
            ).latest('created_at')
        except PasswordResetOTP.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "Bu e-poçta üçin işjeň açar sözü döredilmedi."}
            )

        # Süre kontrolü
        if otp.is_expired:
            raise serializers.ValidationError(
                {"code": "OTP kodyň möhleti geçdi. Täzeden synanyşyň"}
            )

        # Brute-force koruması
        if otp.attempts >= 5:
            raise serializers.ValidationError(
                {"code": "Gaty köp nädogry synanyşyk edildi."}
            )

        # Kod kontrolü
        if otp.code != attrs['code']:
            otp.attempts += 1
            otp.save(update_fields=['attempts'])
            remaining = 5 - otp.attempts
            raise serializers.ValidationError(
                {"code": f"Ýalňyş OTP kody. {remaining} gezek barlama mümkinçiligi galdy."}
            )

        attrs['otp'] = otp
        return attrs

    def save(self):
        otp = self.validated_data['otp']
        new_password = self.validated_data['new_password']

        # Kullanıcıyı bul ve şifreyi güncelle
        try:
            user = User.objects.get(email=otp.email, is_active=True)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "Ulanyjy tapylmady ýa-da hasap işjeň däl."}
            )

        user.set_password(new_password)
        user.save(update_fields=['password'])

        # OTP'yi kullanıldı olarak işaretle
        otp.is_used = True
        otp.save(update_fields=['is_used'])

        # Güvenlik: bu kullanıcının tüm diğer aktif OTP'lerini de geçersiz kıl
        PasswordResetOTP.objects.filter(
            email=otp.email,
            is_used=False,
        ).update(is_used=True)

        return user

class RegisterInitiateSerializer(serializers.Serializer):
    """
    STEP 1: Ulanyjy maglumatlaryny almak we e-poçta salgysyna
    OTP koduny ugratmak
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("E-poçta salgysy hasaba alynan.")
        return value

    def save(self):
        data = self.validated_data
        code = EmailVerification.generate_code()

        verification, _ = EmailVerification.objects.update_or_create(
            email=data['email'],
            defaults={
                'password_hash': make_password(data['password']),
                'code': code,
                'is_verified': False,
                'attempts': 0,
                'expires_at': timezone.now() + timedelta(minutes=10),
            }
        )
        return verification


class RegisterVerifySerializer(serializers.Serializer):
    """
    STEP 2: OTP kody barla, ulanyjy registrasiýa et, token generate et
    """
    email = serializers.EmailField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']

        try:
            verification = EmailVerification.objects.get(email=email, is_verified=False)
        except EmailVerification.DoesNotExist:
            raise serializers.ValidationError(
                {"email": "E-poçta salgysy üçin OTP kody döredilmedi."}
            )

        if verification.is_expired:
            raise serializers.ValidationError(
                {"code": "OTP kodunyň möhleti gutardy, täzeden ugradyň."}
            )

        if verification.attempts >= 5:
            raise serializers.ValidationError(
                {"code": "OTP tassyklama rugsat berilmeýär."}
            )

        if verification.code != code:
            verification.attempts += 1
            verification.save(update_fields=['attempts'])
            remaining = 5 - verification.attempts
            raise serializers.ValidationError(
                {"code": f"Ýalňyş OTP kody. {remaining} gezek barlama mümkinçiligi galdy."}
            )

        attrs['verification'] = verification
        return attrs

    def save(self):
        verification = self.validated_data['verification']

        user = User(
            email=verification.email,
            is_active=True,
        )
        user.password = verification.password_hash
        user.save()

        PoetProfile.objects.create(user=user)

        verification.is_verified = True
        verification.save(update_fields=['is_verified'])

        return user


# ─── REGISTER ─────────────────────────────────────────────────────────────────

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={'min_length': 'Şifre en az 8 karakter olmalıdır.'}
    )
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')
        extra_kwargs = {
            'username': {
                'min_length': 3,
                'error_messages': {'min_length': 'Kullanıcı adı en az 3 karakter olmalıdır.'}
            }
        }

    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError('Bu email adresi zaten kayıtlı.')
        return value.lower()

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('Bu kullanıcı adı zaten alınmış.')
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password_confirm': 'Şifreler eşleşmiyor.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        # PoetProfile otomatik oluşturulur (signal ile de yapılabilir)
        PoetProfile.objects.create(user=user)
        return user


# ─── LOGIN ────────────────────────────────────────────────────────────────────

class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(help_text='Email')
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        login = data.get('login', '').strip()
        password = data.get('password', '')

        if '@' in login:
            try:
                user_obj = User.objects.get(email=login.lower())
                username = user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError('Ulanyjy tapylmady.')

        if user_obj.is_locked_out():
            remaining = user_obj.lockout_until - timezone.now()
            minutes = int(remaining.total_seconds() / 60) + 1
            raise serializers.ValidationError(
                f'Hasabyňyz ýapyldy. {minutes} miuntdan soňra täzeden synanyşyň.'
            )

        # Password verification
        user = authenticate(username=username, password=password)

        if not user:
            user_obj.increment_failed_login()
            raise serializers.ValidationError('Ulanyjy ady ýa-da parol nädogry.')

        if user.is_banned:
            raise serializers.ValidationError('Hasabyňyz banlandy.')

        user.reset_failed_login()
        data['user'] = user
        return data


# ─── POET PROFILE ─────────────────────────────────────────────────────────────

class PoetProfileSerializer(serializers.ModelSerializer):
    poem_count = serializers.ReadOnlyField()

    class Meta:
        model = PoetProfile
        fields = (
            'first_name', 'last_name',
            'instagram', 'tiktok', 'imo',
            'bio', 'avatar', 'avatar_thumbnail',
            'total_score', 'is_private', 'poem_count',
        )
        read_only_fields = ('avatar_thumbnail', 'total_score')


# ─── USER PROFILE (okuma) ─────────────────────────────────────────────────────

class UserProfileSerializer(serializers.ModelSerializer):
    poet_profile = PoetProfileSerializer(read_only=True)
    recent_poems = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'date_joined',
            'is_banned', 'poet_profile', 'recent_poems'
        )
        read_only_fields = ('id', 'email', 'username', 'date_joined', 'is_banned')

    def get_recent_poems(self, obj):
        from apps.poems.serializers import PoemListSerializer
        qs = obj.poems.filter(is_deleted=False, is_draft=False)
        request = self.context.get('request')
        if not request or request.user != obj:
            qs = qs.filter(approve=True)
        poems = qs.order_by('-created_at')[:5]
        return PoemListSerializer(poems, many=True, context=self.context).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')

        # Private profil kontrolü — sadece sahibi görür
        if instance.poet_profile and instance.poet_profile.is_private:
            if not request or request.user != instance:
                data.pop('recent_poems', None)
                data.pop('email', None)

        return data


# ─── PROFILE UPDATE ───────────────────────────────────────────────────────────

class ProfileUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=50,
        required=False,
        allow_blank=True,
        source='poet_profile.first_name'
    )
    last_name = serializers.CharField(
        max_length=50,
        required=False,
        allow_blank=True,
        source='poet_profile.last_name'
    )
    instagram = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        source='poet_profile.instagram'
    )
    tiktok = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        source='poet_profile.tiktok'
    )
    imo = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        source='poet_profile.imo'
    )
    bio = serializers.CharField(
        max_length=500,
        required=False,
        allow_blank=True,
        source='poet_profile.bio'
    )
    is_private = serializers.BooleanField(
        required=False,
        source='poet_profile.is_private'
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'instagram', 'tiktok', 'imo',
            'bio', 'is_private',
        )

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.filter(email=value.lower()).exclude(pk=user.pk).exists():
            raise serializers.ValidationError('Bu email adresi zaten kullanılıyor.')
        return value.lower()

    def update(self, instance, validated_data):
        poet_profile_data = validated_data.pop('poet_profile', {})

        # User alanlarını güncelle
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # PoetProfile alanlarını güncelle
        profile = instance.poet_profile
        for attr, value in poet_profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance


# ─── AVATAR ───────────────────────────────────────────────────────────────────

class AvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField()

    def validate_avatar(self, value):
        return validate_image_file(value)


# ─── CHANGE PASSWORD ──────────────────────────────────────────────────────────

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)
    new_password_confirm = serializers.CharField(write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Mevcut şifre hatalı.')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError({'new_password_confirm': 'Şifreler eşleşmiyor.'})
        return data

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


# ─── BAN ──────────────────────────────────────────────────────────────────────

class BanUserSerializer(serializers.Serializer):
    is_banned = serializers.BooleanField()
    reason = serializers.CharField(required=False, allow_blank=True)


# ─── MINIMAL USER (başka serializer'larda nested kullanım için) ───────────────

class MinimalUserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')

    def get_avatar(self, obj):
        try:
            request = self.context.get('request')
            avatar = obj.poet_profile.avatar
            if avatar and request:
                return request.build_absolute_uri(avatar.url)
        except Exception:
            pass
        return None