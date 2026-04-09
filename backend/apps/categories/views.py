from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.db.models import Count, Q

from .models import Category
from .serializers import CategorySerializer

ACTIVE_POEM_FILTER = Q(
    poems__is_deleted=False,
    poems__is_draft=False,
    poems__approve=True,
)

def get_annotated_queryset():
    return Category.objects.annotate(
        poem_count=Count('poems', filter=ACTIVE_POEM_FILTER)
    ).order_by('name')


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/categories/   → Herkese açık, alfabetik sıra, poem_count ile
    POST /api/categories/   → Sadece admin
    """
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]

    def get_queryset(self):
        return get_annotated_queryset()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/categories/<slug>/  → Herkese açık
    PUT    /api/categories/<slug>/  → Sadece admin
    PATCH  /api/categories/<slug>/  → Sadece admin
    DELETE /api/categories/<slug>/  → Sadece admin
    """
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        return get_annotated_queryset()

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        name = category.name
        # Poem modelinde category FK → on_delete=SET_NULL
        # Django bunu otomatik halleder, şiirler silinmez
        category.delete()
        return Response(
            {
                'message': f'"{name}" kategorisi silindi.',
                'detail': 'Bu kategoriye ait şiirlerin kategori alanı kaldırıldı.'
            },
            status=status.HTTP_200_OK
        )