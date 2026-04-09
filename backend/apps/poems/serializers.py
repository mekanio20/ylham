from rest_framework import serializers
from django.conf import settings
from .models import Poem
from apps.accounts.serializers import MinimalUserSerializer

# ─── LİSTE (özet) ────────────────────────────────────────────────────────────

class PoemListSerializer(serializers.ModelSerializer):
    author = MinimalUserSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    content_preview = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = (
            'id', 'title', 'content_preview', 'author', 'category',
            'tags', 'background_image', 'background_music',
            'public_status', 'poem_note', 'comment_permission',
            'approve',
            'like_count', 'comment_count', 'view_count',
            'is_draft', 'created_at',
        )
        extra_kwargs = {'approve': {'read_only': True}}

    def get_content_preview(self, obj):
        return obj.content[:200]

    def get_category(self, obj):
        if obj.category:
            return {'id': obj.category.id, 'name': obj.category.name, 'slug': obj.category.slug}
        return None

    def get_tags(self, obj):
        return obj.get_tags_list()


# ─── DETAY (tam içerik) ───────────────────────────────────────────────────────

class PoemDetailSerializer(serializers.ModelSerializer):
    author = MinimalUserSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = (
            'id', 'title', 'content', 'author', 'category',
            'tags', 'background_image', 'background_music',
            'public_status', 'poem_note', 'comment_permission',
            'approve',
            'like_count', 'comment_count', 'view_count',
            'user_has_liked', 'is_draft', 'created_at', 'updated_at',
        )
        extra_kwargs = {'approve': {'read_only': True}}

    def get_category(self, obj):
        if obj.category:
            return {'id': obj.category.id, 'name': obj.category.name, 'slug': obj.category.slug}
        return None

    def get_tags(self, obj):
        return obj.get_tags_list()

    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            from apps.interactions.models import PoemLike
            return PoemLike.objects.filter(user=request.user, poem=obj).exists()
        return False


# ─── OLUŞTUR / GÜNCELLE ──────────────────────────────────────────────────────

class PoemCreateUpdateSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(max_length=50),
        required=False,
        default=list,
        help_text='Etiket listesi: ["aşk", "doğa"]'
    )
    category_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Poem
        fields = (
            'title', 'content', 'category_id',
            'tags', 'background_image', 'background_music',
            'public_status', 'poem_note', 'comment_permission', 'is_draft',
        )

    def validate_title(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError('Goşgynyň ady azyndan 2 harp bolmaly.')
        if len(value) > 255:
            raise serializers.ValidationError('Goşgy ady 255 harpdan geçip bilmez.')
        return value

    def validate_content(self, value):
        value = value.strip()
        if len(value) < 20:
            raise serializers.ValidationError('Goşgy azyndan 20 harp bolmaly.')
        return value

    def validate_category_id(self, value):
        if value is not None:
            from apps.categories.models import Category
            if not Category.objects.filter(id=value).exists():
                raise serializers.ValidationError('Degişli kategoriýany saýlaň.')
        return value

    def validate_tags(self, value):
        if len(value) > 10:
            raise serializers.ValidationError('Iň köp 10 tag goşup bolýar.')
        return value

    def create(self, validated_data):
        tags_list = validated_data.pop('tags', [])
        category_id = validated_data.pop('category_id', None)

        poem = Poem(**validated_data)
        poem.author = self.context['request'].user

        if category_id:
            poem.category_id = category_id

        poem.set_tags_from_list(tags_list)
        poem.save()
        return poem

    def update(self, instance, validated_data):
        tags_list = validated_data.pop('tags', None)
        category_id = validated_data.pop('category_id', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if tags_list is not None:
            instance.set_tags_from_list(tags_list)

        if 'category_id' in self.initial_data:
            instance.category_id = category_id

        instance.save()
        return instance