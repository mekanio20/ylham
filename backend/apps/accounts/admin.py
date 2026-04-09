from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PoetProfile


class PoetProfileInline(admin.StackedInline):
    model = PoetProfile
    can_delete = False
    verbose_name = 'Şair Profili'
    fields = (
        'first_name', 'last_name',
        'instagram', 'tiktok', 'imo',
        'bio', 'avatar', 'total_score', 'is_private',
    )
    readonly_fields = ('total_score',)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (PoetProfileInline,)
    list_display = ('username', 'email', 'is_active', 'is_banned', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_banned', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

    # ↓ BaseUserAdmin'in first_name/last_name içeren fieldsets'ini tamamen override et
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Yetkiler', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Güvenlik', {
            'fields': ('is_banned', 'failed_login_attempts', 'lockout_until')
        }),
        ('Önemli tarihler', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Yeni kullanıcı eklerken gösterilecek alanlar
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('date_joined', 'last_login', 'failed_login_attempts', 'lockout_until')


@admin.register(PoetProfile)
class PoetProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'total_score', 'is_private', 'poem_count')
    search_fields = ('user__username', 'first_name', 'last_name', 'instagram', 'tiktok', 'imo')
    readonly_fields = ('total_score',)