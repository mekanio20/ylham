from django.urls import path
from .views import HighlightListView, HighlightSetView, HighlightDeleteView, TopPoetsView

urlpatterns = [
    # Öne çıkan şiirler — ?period=daily/weekly/monthly/yearly
    path('', HighlightListView.as_view(), name='highlight-list'),

    # Admin: manuel highlight ekle/güncelle
    path('set/', HighlightSetView.as_view(), name='highlight-set'),

    # Admin: highlight sil
    path('<int:pk>/', HighlightDeleteView.as_view(), name='highlight-delete'),

    # En iyi şairler
    path('top-poets/', TopPoetsView.as_view(), name='top-poets'),
]