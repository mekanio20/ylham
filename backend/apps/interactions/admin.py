from django.contrib import admin
from .models import PoemLike, Comment, CommentLike


@admin.register(PoemLike)
class PoemLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'poem', 'created_at')
    search_fields = ('user__username', 'poem__title')
    raw_id_fields = ('user', 'poem')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'poem', 'content_preview', 'like_count', 'is_deleted', 'created_at')
    list_filter = ('is_deleted',)
    search_fields = ('user__username', 'poem__title', 'content')
    raw_id_fields = ('user', 'poem')
    readonly_fields = ('like_count', 'created_at', 'updated_at')

    def content_preview(self, obj):
        return obj.content[:60]
    content_preview.short_description = 'İçerik'


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at')
    search_fields = ('user__username',)
    raw_id_fields = ('user', 'comment')