from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    poem = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()
    type_display = serializers.CharField(source='get_notification_type_display', read_only=True)

    class Meta:
        model = Notification
        fields = (
            'id', 'notification_type', 'type_display',
            'sender', 'poem', 'message',
            'is_read', 'created_at'
        )
        read_only_fields = fields

    def get_sender(self, obj):
        if not obj.sender:
            return None
        from apps.accounts.serializers import MinimalUserSerializer
        return MinimalUserSerializer(obj.sender, context=self.context).data

    def get_poem(self, obj):
        if not obj.poem:
            return None
        return {
            'id': obj.poem.id,
            'title': obj.poem.title,
        }

    def get_message(self, obj):
        return obj.get_message()