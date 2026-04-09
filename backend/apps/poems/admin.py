from django.contrib import admin
from .models import Poem, PoemView

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'approve', 'like_count',
        'comment_count', 'view_count', 'is_draft', 'is_deleted', 'created_at'
    )
    list_filter = (
        'approve', 'is_draft', 'is_deleted', 'category',
        'background_music', 'background_image', 'public_status', 'comment_permission'
    )
    search_fields = ('title', 'author__username', 'tags', 'content')
    raw_id_fields = ('author', 'category')
    readonly_fields = ('like_count', 'comment_count', 'view_count', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Esasy maglumatlar', {
            'fields': ('title', 'content', 'author', 'category', 'tags')
        }),
        ('Media', {
            'fields': ('background_image', 'background_music')
        }),
        ('Ýagdaý', {
            'fields': ('is_draft', 'approve', 'public_status', 'comment_permission', 'is_deleted', 'deleted_at')
        }),
        ('Bellik', {
            'fields': ('poem_note',)
        }),
        ('Statistika', {
            'fields': ('like_count', 'comment_count', 'view_count'),
            'classes': ('collapse',)
        }),
        ('Wagt', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['soft_delete_selected', 'restore_selected', 'approve_selected']

    def approve_selected(self, request, queryset):
        updated = queryset.update(approve=True)
        self.message_user(request, f'{updated} goşgy tassyklandy.')
    approve_selected.short_description = 'Saýlananlary tassykla'

    def soft_delete_selected(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(is_deleted=True, deleted_at=timezone.now())
        self.message_user(request, f'{updated} goşgy pozuldy.')
    soft_delete_selected.short_description = 'Saýlananlary pozmak (soft)'

    def restore_selected(self, request, queryset):
        updated = queryset.update(is_deleted=False, deleted_at=None)
        self.message_user(request, f'{updated} goşgy yzyna alyndy.')
    restore_selected.short_description = 'Saýlananlary yzyna al'


@admin.register(PoemView)
class PoemViewAdmin(admin.ModelAdmin):
    list_display = ('poem', 'user', 'ip_address', 'viewed_at')
    search_fields = ('poem__title', 'user__username', 'ip_address')
    raw_id_fields = ('poem', 'user')
    readonly_fields = ('viewed_at',)