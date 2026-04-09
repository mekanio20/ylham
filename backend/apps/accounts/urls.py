from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    TokenRefreshView,
    MyProfileView,
    UserProfileView,
    AvatarUploadView,
    ChangePasswordView,
    BanUserView,
    PoetListView,
    RegisterInitiateView, RegisterVerifyView,
    ForgotPasswordRequestView, ForgotPasswordVerifyView
)

urlpatterns = [
    # Auth
    # path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # Verification
    path('register/initiate/', RegisterInitiateView.as_view(), name='register-initiate'),
    path('register/verify/',   RegisterVerifyView.as_view(),   name='register-verify'),
    # Reset password
    path('forgot-password/',         ForgotPasswordRequestView.as_view(), name='forgot-password-request'),
    path('forgot-password/verify/',  ForgotPasswordVerifyView.as_view(),  name='forgot-password-verify'),

    # Profil
    path('profile/me/', MyProfileView.as_view(), name='my-profile'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),

    # Avatar & Şifre
    path('avatar/', AvatarUploadView.as_view(), name='avatar-upload'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Admin
    path('ban/<int:user_id>/', BanUserView.as_view(), name='ban-user'),

    # Şairler listesi
    path('poets/', PoetListView.as_view(), name='poet-list'),
]