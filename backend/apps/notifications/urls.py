from django.urls import path
from .views import (
    NotificationListView,
    MarkNotificationReadView,
    MarkAllNotificationsReadView,
    UnreadNotificationCountView,
)

urlpatterns = [
    # Bildirim listesi
    path('', NotificationListView.as_view(), name='notification-list'),

    # Okunmamış sayısı — navbar badge için
    path('unread-count/', UnreadNotificationCountView.as_view(), name='notification-unread-count'),

    # Tümünü okundu yap
    path('read-all/', MarkAllNotificationsReadView.as_view(), name='notification-read-all'),

    # Tek bildirimi okundu yap
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='notification-read'),
]