from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Notification
from .serializers import NotificationSerializer
from core.pagination import StandardPagination


class NotificationListView(generics.ListAPIView):
    """
    GET /api/notifications/
    Kullanıcının bildirimlerini listeler.

    Query params:
      ?is_read=true/false     → okunmuş / okunmamış filtresi
      ?type=like/comment/follower/system → tür filtresi
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_queryset(self):
        qs = Notification.objects.filter(
            recipient=self.request.user
        ).select_related('sender', 'sender__poet_profile', 'poem')

        # Okundu / okunmadı filtresi
        is_read = self.request.query_params.get('is_read')
        if is_read is not None:
            if is_read.lower() == 'true':
                qs = qs.filter(is_read=True)
            elif is_read.lower() == 'false':
                qs = qs.filter(is_read=False)

        # Tür filtresi
        notif_type = self.request.query_params.get('type')
        valid_types = [t[0] for t in Notification.NOTIFICATION_TYPES]
        if notif_type and notif_type in valid_types:
            qs = qs.filter(notification_type=notif_type)

        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # Toplam okunmamış sayısını da ekle
        unread_count = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()
        response.data['unread_count'] = unread_count
        return response


class MarkNotificationReadView(APIView):
    """
    POST /api/notifications/<id>/read/
    Tek bir bildirimi okundu olarak işaretle.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        notification = get_object_or_404(
            Notification,
            pk=pk,
            recipient=request.user  # Sadece kendi bildirimi
        )

        if not notification.is_read:
            notification.is_read = True
            notification.save(update_fields=['is_read'])

        return Response({'message': 'Bildirim okundu olarak işaretlendi.'}, status=status.HTTP_200_OK)


class MarkAllNotificationsReadView(APIView):
    """
    POST /api/notifications/read-all/
    Tüm bildirimleri okundu olarak işaretle.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        updated = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).update(is_read=True)

        return Response(
            {'message': f'{updated} bildirim okundu olarak işaretlendi.'},
            status=status.HTTP_200_OK
        )


class UnreadNotificationCountView(APIView):
    """
    GET /api/notifications/unread-count/
    Okunmamış bildirim sayısını döner.
    Navbar badge için kullanışlı.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()
        return Response({'unread_count': count})