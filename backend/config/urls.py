from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Swagger / OpenAPI
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ── Swagger / OpenAPI ────────────────────────────────────────────────────
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Auth & Kullanıcı
    path('api/auth/', include('apps.accounts.urls')),

    # Kategoriler
    path('api/categories/', include('apps.categories.urls')),

    # Şiirler
    path('api/poems/', include('apps.poems.urls')),

    # Bildirimler
    path('api/notifications/', include('apps.notifications.urls')),

    # Öne Çıkanlar
    path('api/highlights/', include('apps.highlights.urls')),

    # Arama
    path('api/search/', include('apps.search.urls')),
    
    # Etkileşimler (beğeni, yorum)
    path('api/', include('apps.interactions.urls')),
]

# Geliştirme ortamında media dosyalarını sun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)