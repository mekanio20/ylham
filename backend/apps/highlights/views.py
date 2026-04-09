from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Highlight
from .serializers import HighlightSerializer, HighlightSetSerializer


class HighlightListView(generics.ListAPIView):
    """
    GET /api/highlights/?period=daily
    GET /api/highlights/?period=weekly
    GET /api/highlights/?period=monthly
    GET /api/highlights/?period=yearly

    Period belirtilmezse daily döner.
    Herkese açık, sıralamaya göre 1-10 arası.
    """
    serializer_class = HighlightSerializer
    permission_classes = [AllowAny]
    pagination_class = None  # Highlight listesi zaten max 10, pagination gereksiz

    def get_queryset(self):
        period = self.request.query_params.get('period', 'daily')

        valid_periods = [p[0] for p in Highlight.PERIOD_CHOICES]
        if period not in valid_periods:
            period = 'daily'

        return Highlight.objects.filter(
            period=period,
            poem__is_deleted=False,
            poem__is_draft=False,
            poem__approve=True,
            poem__author__is_banned=False,
        ).select_related(
            'poem', 'poem__author', 'poem__author__poet_profile', 'poem__category'
        ).order_by('rank')


class HighlightSetView(APIView):
    """
    POST /api/highlights/set/
    Admin manuel highlight ekler veya günceller (upsert).
    Body: { "poem_id": 1, "period": "daily", "rank": 1 }

    Aynı period+rank varsa üzerine yazar (eski kayıt silinmez, güncellenir).
    """
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = HighlightSetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        poem_id = data['poem_id']
        period = data['period']
        rank = data['rank']

        from apps.poems.models import Poem
        poem = Poem.objects.get(id=poem_id)

        # Upsert — aynı period+rank varsa güncelle, yoksa oluştur
        highlight, created = Highlight.objects.update_or_create(
            period=period,
            rank=rank,
            defaults={
                'poem': poem,
                'is_manual': True,
                'selected_by': request.user,
                'score': poem.view_count + (poem.like_count * 3),
            }
        )

        action = 'oluşturuldu' if created else 'güncellendi'
        return Response(
            {
                'message': f'Highlight {action}.',
                'data': HighlightSerializer(highlight, context={'request': request}).data
            },
            status=status.HTTP_200_OK
        )


class HighlightDeleteView(APIView):
    """
    DELETE /api/highlights/<id>/
    Admin bir highlight kaydını siler.
    """
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        try:
            highlight = Highlight.objects.get(pk=pk)
        except Highlight.DoesNotExist:
            return Response({'error': 'Highlight bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)

        highlight.delete()
        return Response({'message': 'Highlight silindi.'}, status=status.HTTP_200_OK)


class TopPoetsView(generics.ListAPIView):
    """
    GET /api/highlights/top-poets/
    En yüksek puanlı şairleri listeler.
    Herkese açık.
    """
    permission_classes = [AllowAny]
    pagination_class = None

    def get(self, request):
        from apps.accounts.models import PoetProfile
        from apps.accounts.serializers import MinimalUserSerializer

        top_poets = PoetProfile.objects.filter(
            user__is_banned=False,
            user__is_active=True,
        ).select_related('user').order_by('-total_score')[:10]

        result = []
        for profile in top_poets:
            result.append({
                'user': MinimalUserSerializer(profile.user, context={'request': request}).data,
                'total_score': profile.total_score,
                'poem_count': profile.poem_count,
                'bio': profile.bio,
            })

        return Response(result)