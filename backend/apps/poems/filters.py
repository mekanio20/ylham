import django_filters
from .models import Poem

class PoemFilter(django_filters.FilterSet):
    # Başlık içinde arama
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    # Yazar username ile filtrele
    author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')

    # Kategori slug ile filtrele
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')

    # Tag içinde arama
    tag = django_filters.CharFilter(field_name='tags', lookup_expr='icontains')

    class Meta:
        model = Poem
        fields = ['title', 'author', 'category', 'tag']