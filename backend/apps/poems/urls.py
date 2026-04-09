from django.urls import path
from .views import (
    PoemListView,
    PoemCreateView,
    PoemDetailView,
    PoemUpdateView,
    PoemDeleteView,
    DraftListView,
    DraftPublishView,
    MyPoemsView,
)

urlpatterns = [
    # Ana liste ve oluşturma
    path('', PoemListView.as_view(), name='poem-list'),
    path('create/', PoemCreateView.as_view(), name='poem-create'),

    # Kendi şiirleri
    path('mine/', MyPoemsView.as_view(), name='my-poems'),

    # Taslaklar
    path('drafts/', DraftListView.as_view(), name='draft-list'),

    # Tekil şiir işlemleri
    path('<int:pk>/', PoemDetailView.as_view(), name='poem-detail'),
    path('<int:pk>/update/', PoemUpdateView.as_view(), name='poem-update'),
    path('<int:pk>/delete/', PoemDeleteView.as_view(), name='poem-delete'),
    path('<int:pk>/publish/', DraftPublishView.as_view(), name='poem-publish'),
]