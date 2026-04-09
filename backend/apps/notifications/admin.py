from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read')
    search_fields = ('recipient__username', 'sender__username')
    raw_id_fields = ('recipient', 'sender', 'poem')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} bildirim okundu olarak işaretlendi.')
    mark_as_read.short_description = 'Seçilenleri okundu yap'