from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from .models import User, PasswordResetOTP
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    ProfileUpdateSerializer,
    AvatarSerializer,
    ChangePasswordSerializer,
    BanUserSerializer,
    RegisterInitiateSerializer, RegisterVerifySerializer,
    ForgotPasswordRequestSerializer, ForgotPasswordVerifySerializer
)
from core.utils import optimize_image, create_thumbnail

class ForgotPasswordRequestView(APIView):
    """
    POST /auth/forgot-password/
    Body: { "email": "user@example.com" }

    Elektron poçta ulgamyň içinde ýazylan bolsa, OTP iberiler.
    Elektron poçta ýok bolsa-da, şol bir üstünlikli habar berler (howpsuzlyk üçin).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        # Kullanıcı varsa OTP oluştur ve gönder
        user = User.objects.filter(email=email, is_active=True).first()
        if user:
            self._create_and_send_otp(email)

        # Kullanıcı olmasa bile aynı mesajı dön — user enumeration önlemi
        return Response(
            {
                "message": (
                    f"{email} salgysyna 6 belgili tassyklama kody ugradyldy."
                )
            },
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def _create_and_send_otp(email: str):
        code = PasswordResetOTP.generate_code()

        # Varolan kullanılmamış OTP'leri geçersiz kıl, yenisini oluştur
        PasswordResetOTP.objects.filter(email=email, is_used=False).update(is_used=True)

        PasswordResetOTP.objects.create(email=email, code=code)

        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
                <div style="max-width: 500px; margin: auto; background: white; padding: 30px; border-radius: 10px; text-align: center;">
                    
                    <h2 style="color: #333;">Tassyklama kody</h2>
                    
                    <p style="font-size: 16px; color: #555;">
                        Salam,
                    </p>
                    
                    <p style="font-size: 16px; color: #555;">
                        Ylham platformasy tarapyndan ugradylan tassyklama kodyňyz:
                    </p>
                    
                    <div style="font-size: 34px; font-weight: bold; color: #2c7be5; margin: 20px 0; letter-spacing: 3px;">
                        {code}
                    </div>
                    
                    <p style="font-size: 14px; color: #888;">
                        Bu kod <b>10 minutdan</b> soň güýjini ýitirer.
                    </p>
                </div>
            </body>
        </html>
        """

        send_mail(
            subject="Ylham tassyklama kodyňyz",
            message="HTML goldaýan e-poçta ulanyň.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
            html_message=html_content
        )

class ForgotPasswordVerifyView(APIView):
    """
    POST /auth/forgot-password/verify/
    Body: {
        "email": "user@example.com",
        "code": "123456",
        "new_password": "newpass123",
        "new_password_confirm": "newpass123"
    }
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "Açar sözüňiz üstünlikli täzelendi.",
                "username": user.username,
            },
            status=status.HTTP_200_OK,
        )

class RegisterInitiateView(APIView):
    """
    POST /auth/register/initiate/
    Ulanyjy maglumatlaryny alyp, 6 belgili tassyklama kodyny email salgysyna ugradar
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterInitiateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        verification = serializer.save()

        # E-posta gönder
        self._send_verification_email(verification.email, verification.code)

        return Response(
            {
                "message": (
                    f"{verification.email} salgysyna 6 belgili tassyklama kody ugradyldy. "
                    "Kodyň möhleti 10 minut."
                ),
                "email": verification.email,
            },
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def _send_verification_email(email: str, code: str):
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
                <div style="max-width: 500px; margin: auto; background: white; padding: 30px; border-radius: 10px; text-align: center;">
                    
                    <h2 style="color: #333;">Tassyklama kody</h2>
                    
                    <p style="font-size: 16px; color: #555;">
                        Salam,
                    </p>
                    
                    <p style="font-size: 16px; color: #555;">
                        Ylham platformasy tarapyndan ugradylan tassyklama kodyňyz:
                    </p>
                    
                    <div style="font-size: 34px; font-weight: bold; color: #2c7be5; margin: 20px 0; letter-spacing: 3px;">
                        {code}
                    </div>
                    
                    <p style="font-size: 14px; color: #888;">
                        Bu kod <b>10 minutdan</b> soň güýjini ýitirer.
                    </p>
                </div>
            </body>
        </html>
        """

        send_mail(
            subject="Ylham tassyklama kodyňyz",
            message="HTML goldaýan e-poçta ulanyň.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
            html_message=html_content
        )


class RegisterVerifyView(APIView):
    """
    POST /auth/register/verify/
    Ulanyjyny tassyklar, JWT token generate eder
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Üstünlikli.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "tokens": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
            },
            status=status.HTTP_201_CREATED,
        )

# ─── REGISTER ─────────────────────────────────────────────────────────────────

class RegisterView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    Yeni kullanıcı kaydı. PoetProfile otomatik oluşturulur.
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Kayıt sonrası otomatik token üret
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'Kayıt başarılı.',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_201_CREATED)


# ─── LOGIN ────────────────────────────────────────────────────────────────────

class LoginView(APIView):
    """
    POST /api/auth/login/
    Username veya email + şifre ile giriş. JWT token döner.
    Brute force koruması: 5 yanlış denemede 15 dk kilit.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'Üstülinkli',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff,
            },
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)


# ─── LOGOUT ───────────────────────────────────────────────────────────────────

class LogoutView(APIView):
    """
    POST /api/auth/logout/
    Refresh token'ı blacklist'e ekler.
    Body: { "refresh": "<refresh_token>" }
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(
                {'error': 'Refresh token gereklidir.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Çıkış başarılı.'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response(
                {'error': 'Geçersiz veya süresi dolmuş token.'},
                status=status.HTTP_400_BAD_REQUEST
            )


# ─── TOKEN REFRESH ────────────────────────────────────────────────────────────

from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView

class TokenRefreshView(BaseTokenRefreshView):
    """
    POST /api/auth/token/refresh/
    Refresh token ile yeni access token üretir.
    Body: { "refresh": "<refresh_token>" }
    """
    permission_classes = [AllowAny]


# ─── PROFILE ──────────────────────────────────────────────────────────────────

class MyProfileView(generics.RetrieveUpdateAPIView):
    """
    GET  /api/auth/profile/me/  → kendi profilim
    PUT  /api/auth/profile/me/  → profilimi güncelle
    """
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return ProfileUpdateSerializer
        return UserProfileSerializer

    def get_object(self):
        return self.request.user


class UserProfileView(generics.RetrieveAPIView):
    """
    GET /api/auth/profile/<username>/
    Başka bir kullanıcının profilini görüntüle.
    Yasaklı veya private profiller kontrol edilir.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'
    queryset = User.objects.select_related('poet_profile').filter(is_active=True)

    def get_object(self):
        user = get_object_or_404(
            User,
            username=self.kwargs['username'],
            is_active=True
        )

        if user.is_banned:
            from rest_framework.exceptions import NotFound
            raise NotFound('Bu kullanıcı profili mevcut değil.')

        return user


# ─── AVATAR ───────────────────────────────────────────────────────────────────

class AvatarUploadView(APIView):
    """
    POST /api/auth/avatar/
    Avatar yükle: optimize eder, thumbnail oluşturur.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AvatarSerializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)

        avatar_file = serializer.validated_data['avatar']
        profile = request.user.poet_profile

        # Orijinal resmi optimize et
        optimized = optimize_image(avatar_file)
        filename = f'avatar_{request.user.id}.jpg'
        profile.avatar.save(filename, ContentFile(optimized.read()), save=False)

        # Thumbnail oluştur
        avatar_file.seek(0)
        thumbnail = create_thumbnail(avatar_file)
        thumb_filename = f'thumb_{request.user.id}.jpg'
        profile.avatar_thumbnail.save(thumb_filename, ContentFile(thumbnail.read()), save=False)

        profile.save()

        return Response({
            'message': 'Avatar güncellendi.',
            'avatar': request.build_absolute_uri(profile.avatar.url),
            'avatar_thumbnail': request.build_absolute_uri(profile.avatar_thumbnail.url),
        }, status=status.HTTP_200_OK)


# ─── CHANGE PASSWORD ──────────────────────────────────────────────────────────

class ChangePasswordView(APIView):
    """
    POST /api/auth/change-password/
    Eski şifreyi doğrular, yeni şifreyi kaydeder.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Şifre başarıyla değiştirildi.'}, status=status.HTTP_200_OK)


# ─── BAN USER (Admin) ─────────────────────────────────────────────────────────

class BanUserView(APIView):
    """
    POST /api/auth/ban/<user_id>/
    Admin bir şairi yasaklar veya yasağı kaldırır.
    Body: { "is_banned": true/false }
    """
    permission_classes = [IsAdminUser]

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        if user.is_staff:
            return Response(
                {'error': 'Admin kullanıcılar yasaklanamaz.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BanUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user.is_banned = serializer.validated_data['is_banned']
        user.save(update_fields=['is_banned'])

        action = 'yasaklandı' if user.is_banned else 'yasağı kaldırıldı'
        return Response({
            'message': f'{user.username} kullanıcısı {action}.',
            'is_banned': user.is_banned,
        }, status=status.HTTP_200_OK)


# ─── LIST POETS ───────────────────────────────────────────────────────────────

class PoetListView(generics.ListAPIView):
    """
    GET /api/auth/poets/
    Tüm şairleri listele. Sıralama: ?ordering=total_score, -date_joined, username
    """
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.select_related('poet_profile').filter(
            is_active=True,
            is_banned=False,
        ).order_by('-poet_profile__total_score')