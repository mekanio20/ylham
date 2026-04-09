from django.urls import path
from .views import SimpleSearchView, AdvancedSearchView, PoetSearchView

urlpatterns = [
    # Basit arama — ?q=aşk
    path('', SimpleSearchView.as_view(), name='simple-search'),

    # Gelişmiş arama — ?q=&title=&author=&category=&tag=&ordering=
    path('advanced/', AdvancedSearchView.as_view(), name='advanced-search'),

    # Şair arama — ?q=ahmet
    path('poets/', PoetSearchView.as_view(), name='poet-search'),
]