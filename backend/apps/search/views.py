from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q, Case, When, IntegerField, Value

from apps.poems.models import Poem
from apps.poems.serializers import PoemListSerializer
from apps.accounts.models import User
from apps.accounts.serializers import MinimalUserSerializer
from core.pagination import StandardPagination


# ─── YARDIMCI: aktif şiir queryset ───────────────────────────────────────────

def active_poems():
    return Poem.objects.filter(
        is_deleted=False,
        is_draft=False,
        approve=True,
        author__is_banned=False,
    ).select_related('author', 'author__poet_profile', 'category')


# ─── BASİT ARAMA ─────────────────────────────────────────────────────────────

class SimpleSearchView(APIView):
    """
    GET /api/search/?q=aşk

    Şiir başlığı, yazar adı ve tag içinde arama yapar.
    Sonuçlar relevance'a göre sıralanır:
      - Başlıkta eşleşme → en yüksek öncelik
      - Tag'de eşleşme   → orta öncelik
      - Yazar adında     → düşük öncelik
    """
    permission_classes = [AllowAny]
    pagination_class = StandardPagination

    def get(self, request):
        q = request.query_params.get('q', '').strip()

        if not q:
            return Response({'results': [], 'count': 0})

        if len(q) < 2:
            return Response(
                {'error': 'Arama terimi en az 2 karakter olmalıdır.'},
                status=400
            )

        queryset = active_poems().filter(
            Q(title__icontains=q) |
            Q(tags__icontains=q) |
            Q(author__username__icontains=q)
        ).annotate(
            # Relevance skoru: başlık eşleşmesi > tag > yazar
            relevance=Case(
                When(title__icontains=q, then=Value(3)),
                When(tags__icontains=q, then=Value(2)),
                When(author__username__icontains=q, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by('-relevance', '-like_count', '-created_at').distinct()

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        serializer = PoemListSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


# ─── GELİŞMİŞ ARAMA ─────────────────────────────────────────────────────────

class AdvancedSearchView(APIView):
    """
    GET /api/search/advanced/

    Query params:
      q        → genel arama (başlık + içerik + tag + yazar)
      title    → sadece başlıkta ara
      author   → sadece yazar adında ara
      category → kategori slug
      tag      → etiket içinde ara
      ordering → created_at | like_count | view_count | -created_at (default)
    """
    permission_classes = [AllowAny]
    pagination_class = StandardPagination

    def get(self, request):
        q        = request.query_params.get('q', '').strip()
        title    = request.query_params.get('title', '').strip()
        author   = request.query_params.get('author', '').strip()
        category = request.query_params.get('category', '').strip()
        tag      = request.query_params.get('tag', '').strip()
        ordering = request.query_params.get('ordering', '-created_at')

        # En az bir parametre zorunlu
        if not any([q, title, author, category, tag]):
            return Response(
                {'error': 'En az bir arama parametresi giriniz.'},
                status=400
            )

        queryset = active_poems()

        # Genel q → başlık + içerik + tag + yazar
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(tags__icontains=q) |
                Q(author__username__icontains=q)
            )

        # Tekil filtreler (kombinasyon destekli)
        if title:
            queryset = queryset.filter(title__icontains=title)

        if author:
            queryset = queryset.filter(author__username__icontains=author)

        if category:
            queryset = queryset.filter(category__slug=category)

        if tag:
            queryset = queryset.filter(tags__icontains=tag)

        # Sıralama doğrulama
        valid_orderings = [
            'created_at', '-created_at',
            'like_count', '-like_count',
            'view_count', '-view_count',
            'comment_count', '-comment_count',
        ]
        if ordering not in valid_orderings:
            ordering = '-created_at'

        queryset = queryset.order_by(ordering).distinct()

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        serializer = PoemListSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


# ─── ŞAİR ARAMA ──────────────────────────────────────────────────────────────

class PoetSearchView(APIView):
    """
    GET /api/search/poets/?q=ahmet

    Şair adında arama yapar.
    """
    permission_classes = [AllowAny]
    pagination_class = StandardPagination

    def get(self, request):
        q = request.query_params.get('q', '').strip()

        if not q or len(q) < 2:
            return Response(
                {'error': 'Arama terimi en az 2 karakter olmalıdır.'},
                status=400
            )

        queryset = User.objects.filter(
            username__icontains=q,
            is_active=True,
            is_banned=False,
        ).select_related('poet_profile').order_by('username')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        serializer = MinimalUserSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)