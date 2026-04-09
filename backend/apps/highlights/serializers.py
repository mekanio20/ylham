from rest_framework import serializers
from .models import Highlight


class HighlightSerializer(serializers.ModelSerializer):
    poem = serializers.SerializerMethodField()
    period_display = serializers.CharField(source='get_period_display', read_only=True)

    class Meta:
        model = Highlight
        fields = (
            'id', 'period', 'period_display', 'rank',
            'score', 'is_manual', 'poem', 'created_at'
        )
        read_only_fields = ('id', 'score', 'created_at', 'period_display')

    def get_poem(self, obj):
        from apps.poems.serializers import PoemListSerializer
        return PoemListSerializer(obj.poem, context=self.context).data


class HighlightSetSerializer(serializers.Serializer):
    """Admin manuel highlight ayarlamak için."""
    poem_id = serializers.IntegerField()
    period = serializers.ChoiceField(choices=Highlight.PERIOD_CHOICES)
    rank = serializers.IntegerField(min_value=1, max_value=10)

    def validate_poem_id(self, value):
        from apps.poems.models import Poem
        if not Poem.objects.filter(
            id=value, is_deleted=False, is_draft=False, approve=True
        ).exists():
            raise serializers.ValidationError('Geçerli ve yayınlanmış bir şiir ID\'si giriniz.')
        return value

    def validate(self, data):
        # Aynı period + rank kombinasyonu varsa güncelleme yapılacak (upsert)
        return data