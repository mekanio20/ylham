from django.urls import path
from .views import (
    PoemLikeToggleView,
    CommentListCreateView,
    CommentDetailView,
    CommentLikeToggleView,
    PoemInteractionStatsView,
)

urlpatterns = [
    # Şiir beğeni toggle
    path('poems/<int:poem_id>/like/', PoemLikeToggleView.as_view(), name='poem-like-toggle'),

    # Şiir yorumları
    path('poems/<int:poem_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),

    # Tekil yorum
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    # Yorum beğeni toggle
    path('comments/<int:comment_id>/like/', CommentLikeToggleView.as_view(), name='comment-like-toggle'),

    # Şiir istatistikleri
    path('poems/<int:poem_id>/stats/', PoemInteractionStatsView.as_view(), name='poem-stats'),
]