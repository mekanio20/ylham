from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated, AllowAny)
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.utils import timezone

from .models import Poem, PoemView
from .serializers import PoemListSerializer, PoemDetailSerializer, PoemCreateUpdateSerializer
from .filters import PoemFilter
from core.permissions import IsNotBanned
from core.pagination import StandardPagination
from core.utils import update_poet_score
from django.conf import settings


# ─── YARDIMCI: görüntülenme kaydet ───────────────────────────────────────────

def record_view(poem, request):
    """
    Aynı kullanıcı / IP'nin aynı şiiri birden fazla sayılmaması için
    PoemView kaydı oluşturur. Yeni kayıtsa view_count artırılır.
    """
    user = request.user if request.user.is_authenticated else None
    ip = get_client_ip(request)

    try:
        if user:
            _, created = PoemView.objects.get_or_create(poem=poem, user=user)
        else:
            _, created = PoemView.objects.get_or_create(poem=poem, ip_address=ip, user=None)

        if created:
            Poem.objects.filter(pk=poem.pk).update(view_count=poem.view_count + 1)
            update_poet_score(poem.author, settings.SCORE_PER_VIEW)
    except Exception:
        pass  # Görüntülenme hatası şiiri engellemesin


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


# ─── ŞİİR LİSTELE ────────────────────────────────────────────────────────────

class PoemListView(generics.ListAPIView):
    """
    GET /api/poems/
    Tüm yayınlanmış şiirleri listeler. Sayfalama, filtreleme, sıralama.

    Filtreleme: ?title=&author=&category=&tag=
    Sıralama:   ?ordering=-created_at | -like_count | -view_count
    """
    serializer_class = PoemListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PoemFilter
    search_fields = ['title', 'author__username', 'tags']
    ordering_fields = ['created_at', 'like_count', 'view_count', 'comment_count']
    ordering = ['-created_at']

    def get_queryset(self):
        return Poem.objects.filter(
            is_deleted=False,
            is_draft=False,
            approve=True,
            author__is_banned=False,
        ).select_related(
            'author', 'author__poet_profile', 'category'
        )


# ─── ŞİİR OLUŞTUR ────────────────────────────────────────────────────────────

class PoemCreateView(generics.CreateAPIView):
    """
    POST /api/poems/
    Yeni şiir oluştur. is_draft=true ile taslak kaydedilebilir.
    """
    serializer_class = PoemCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsNotBanned]

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        poem = serializer.save()
        output = PoemDetailSerializer(poem, context={'request': request})
        return Response(output.data, status=status.HTTP_201_CREATED)


# ─── ŞİİR DETAY ──────────────────────────────────────────────────────────────

class PoemDetailView(generics.RetrieveAPIView):
    """
    GET /api/poems/<id>/
    Şiir detayını getirir, görüntülenme sayısını artırır.
    """
    serializer_class = PoemDetailSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        poem = get_object_or_404(
            Poem,
            pk=self.kwargs['pk'],
            is_deleted=False,
        )

        # Yasaklı yazarın şiiri
        if poem.author.is_banned:
            from rest_framework.exceptions import NotFound
            raise NotFound('Şiir bulunamadı.')

        if not poem.is_visible_to(self.request.user):
            from rest_framework.exceptions import NotFound
            raise NotFound('Şiir bulunamadı.')

        return poem

    def retrieve(self, request, *args, **kwargs):
        poem = self.get_object()
        record_view(poem, request)
        serializer = self.get_serializer(poem)
        return Response(serializer.data)


# ─── ŞİİR GÜNCELLE ───────────────────────────────────────────────────────────

class PoemUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/poems/<id>/
    Sadece şiirin yazarı güncelleyebilir.
    """
    serializer_class = PoemCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsNotBanned]

    def get_object(self):
        poem = get_object_or_404(Poem, pk=self.kwargs['pk'], is_deleted=False)

        if poem.author != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied('Bu şiiri düzenleme yetkiniz yok.')

        return poem

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        poem = self.get_object()
        serializer = self.get_serializer(poem, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        updated_poem = serializer.save()
        output = PoemDetailSerializer(updated_poem, context={'request': request})
        return Response(output.data)


# ─── ŞİİR SİL ────────────────────────────────────────────────────────────────

class PoemDeleteView(APIView):
    """
    DELETE /api/poems/<id>/
    - Yazar: soft delete (is_deleted=True)
    - Admin: hard delete (tamamen siler)
    """
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def delete(self, request, pk):
        poem = get_object_or_404(Poem, pk=pk, is_deleted=False)

        # Yazar veya admin kontrolü
        if not request.user.is_staff and poem.author != request.user:
            return Response(
                {'error': 'Bu şiiri silme yetkiniz yok.'},
                status=status.HTTP_403_FORBIDDEN
            )

        if request.user.is_staff:
            # Admin → hard delete
            poem.delete()
            return Response({'message': 'Şiir kalıcı olarak silindi.'}, status=status.HTTP_200_OK)
        else:
            # Yazar → soft delete
            poem.is_deleted = True
            poem.deleted_at = timezone.now()
            poem.save(update_fields=['is_deleted', 'deleted_at'])

            # Highlight listesinden kaldır
            from apps.highlights.models import Highlight
            Highlight.objects.filter(poem=poem).delete()

            return Response({'message': 'Şiir silindi.'}, status=status.HTTP_200_OK)


# ─── TASLAK LİSTELE ──────────────────────────────────────────────────────────

class DraftListView(generics.ListAPIView):
    """
    GET /api/poems/drafts/
    Sadece giriş yapmış kullanıcının kendi taslaklarını listeler.
    """
    serializer_class = PoemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_queryset(self):
        return Poem.objects.filter(
            author=self.request.user,
            is_draft=True,
            is_deleted=False,
        ).select_related('author', 'author__poet_profile', 'category').order_by('-created_at')


# ─── TASLAKTAN YAYINLA ────────────────────────────────────────────────────────

class DraftPublishView(APIView):
    """
    POST /api/poems/<id>/publish/
    Taslak şiiri yayınlar.
    """
    permission_classes = [IsAuthenticated, IsNotBanned]

    def post(self, request, pk):
        poem = get_object_or_404(
            Poem,
            pk=pk,
            author=request.user,
            is_draft=True,
            is_deleted=False,
        )
        poem.is_draft = False
        poem.save(update_fields=['is_draft', 'updated_at'])
        output = PoemDetailSerializer(poem, context={'request': request})
        return Response(
            {'message': 'Şiir yayınlandı.', 'poem': output.data},
            status=status.HTTP_200_OK
        )


# ─── KENDİ ŞİİRLERİM ─────────────────────────────────────────────────────────

class MyPoemsView(generics.ListAPIView):
    """
    GET /api/poems/mine/
    Giriş yapmış kullanıcının kendi tüm şiirleri (taslak dahil, silinmiş hariç).
    """
    serializer_class = PoemListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at', 'like_count', 'view_count']
    ordering = ['-created_at']

    def get_queryset(self):
        return Poem.objects.filter(
            author=self.request.user,
            is_deleted=False,
        ).select_related('author', 'author__poet_profile', 'category')