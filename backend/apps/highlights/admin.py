from django.contrib import admin
from .models import Highlight


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('rank', 'period', 'poem', 'score', 'is_manual', 'selected_by', 'created_at')
    list_filter = ('period', 'is_manual')
    search_fields = ('poem__title', 'poem__author__username')
    ordering = ('period', 'rank')
    readonly_fields = ('score', 'created_at')
    raw_id_fields = ('poem', 'selected_by')