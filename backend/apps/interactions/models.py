from django.db import models
from django.conf import settings


class PoemLike(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='poem_likes'
    )
    poem = models.ForeignKey(
        'poems.Poem',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'poem_likes'
        verbose_name = 'Şiir Beğenisi'
        verbose_name_plural = 'Şiir Beğenileri'
        unique_together = ('user', 'poem')

    def __str__(self):
        return f'{self.user.username} → {self.poem.title}'


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    poem = models.ForeignKey(
        'poems.Poem',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(max_length=500)
    like_count = models.PositiveIntegerField(default=0)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} → {self.poem.title}: {self.content[:50]}'


class CommentLike(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_likes'
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment_likes'
        verbose_name = 'Yorum Beğenisi'
        verbose_name_plural = 'Yorum Beğenileri'
        unique_together = ('user', 'comment')

    def __str__(self):
        return f'{self.user.username} → yorum #{self.comment.id}'