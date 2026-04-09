from rest_framework import serializers
from .models import Comment, CommentLike, PoemLike


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'content', 'like_count',
            'user_has_liked', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'author', 'like_count', 'created_at', 'updated_at')

    def get_author(self, obj):
        from apps.accounts.serializers import MinimalUserSerializer
        return MinimalUserSerializer(obj.user, context=self.context).data

    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return CommentLike.objects.filter(user=request.user, comment=obj).exists()
        return False


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

    def validate_content(self, value):
        value = value.strip()
        if len(value) < 1:
            raise serializers.ValidationError('Yorum boş olamaz.')
        if len(value) > 500:
            raise serializers.ValidationError('Yorum en fazla 500 karakter olabilir.')
        return value


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

    def validate_content(self, value):
        value = value.strip()
        if len(value) < 1:
            raise serializers.ValidationError('Yorum boş olamaz.')
        if len(value) > 500:
            raise serializers.ValidationError('Yorum en fazla 500 karakter olabilir.')
        return value


class PoemInteractionStatsSerializer(serializers.Serializer):
    """Şiir etkileşim istatistikleri."""
    poem_id = serializers.IntegerField()
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()
    view_count = serializers.IntegerField()
    user_has_liked = serializers.BooleanField()