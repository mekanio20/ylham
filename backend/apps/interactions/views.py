from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models import F, Case, When, Value
from django.utils import timezone

from apps.poems.models import Poem
from .models import PoemLike, Comment, CommentLike
from .serializers import (
    CommentSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
    PoemInteractionStatsSerializer,
)
from core.permissions import IsNotBanned, IsOwnerOrAdmin
from core.pagination import StandardPagination
from core.utils import update_poet_score
from django.conf import settings


# ─── helpers ─────────────────────────────────────────────────────────────────

def send_notification(recipient, sender, notif_type, poem=None):
    """Bildirim oluştur — kendi eylemine bildirim gönderme."""
    if recipient == sender:
        return
    try:
        from apps.notifications.models import Notification
        Notification.objects.create(
            recipient=recipient,
            sender=sender,
            notification_type=notif_type,
            poem=poem,
        )
    except Exception:
        pass


# ─── ŞİİR BEĞENİ TOGGLE ──────────────────────────────────────────────────────

class PoemLikeToggleView(APIView):
    """
    POST /api/poems/<poem_id>/like/
    Beğen / beğeniyi kaldır (toggle).
    """
    permission_classes = [IsAuthenticated, IsNotBanned]

    @transaction.atomic
    def post(self, request, poem_id):
        poem = get_object_or_404(
            Poem,
            id=poem_id,
            is_deleted=False,
            is_draft=False,
        )

        if not poem.is_visible_to(request.user):
            from rest_framework.exceptions import NotFound
            raise NotFound('Goşgy tapylmady.')

        if poem.author.is_banned:
            return Response(
                {'error': 'Bu şiire etkileşim yapılamaz.'},
                status=status.HTTP_403_FORBIDDEN
            )

        like, created = PoemLike.objects.get_or_create(
            user=request.user,
            poem=poem,
        )

        if created:
            # ✅ F() ile race condition olmadan artır
            Poem.objects.filter(pk=poem.pk).update(like_count=F('like_count') + 1)
            update_poet_score(poem.author, settings.SCORE_PER_LIKE)
            send_notification(poem.author, request.user, 'like', poem=poem)

            poem.refresh_from_db()
            return Response(
                {'liked': True, 'like_count': poem.like_count},
                status=status.HTTP_201_CREATED
            )
        else:
            like.delete()
            # ✅ F() ile azalt, 0'ın altına düşme
            Poem.objects.filter(pk=poem.pk).update(
                like_count=Case(
                    When(like_count__gt=0, then=F('like_count') - 1),
                    default=Value(0),
                )
            )
            update_poet_score(poem.author, -settings.SCORE_PER_LIKE)

            poem.refresh_from_db()
            return Response(
                {'liked': False, 'like_count': poem.like_count},
                status=status.HTTP_200_OK
            )


# ─── YORUM LİSTELE / OLUŞTUR ─────────────────────────────────────────────────

class CommentListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/poems/<poem_id>/comments/
    POST /api/poems/<poem_id>/comments/
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsNotBanned()]
        return [IsAuthenticatedOrReadOnly()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        poem_id = self.kwargs['poem_id']
        poem = get_object_or_404(Poem, id=poem_id, is_deleted=False)
        if not poem.is_visible_to(self.request.user):
            from rest_framework.exceptions import NotFound
            raise NotFound('Goşgy tapylmady.')

        ordering = self.request.query_params.get('ordering', 'created_at')

        valid_orderings = ['-created_at', 'created_at', '-like_count', 'like_count']
        if ordering not in valid_orderings:
            ordering = 'created_at'

        return Comment.objects.filter(
            poem_id=poem_id,
            poem__is_deleted=False,
            is_deleted=False,
        ).select_related('user', 'user__poet_profile').order_by(ordering)

    @transaction.atomic
    def perform_create(self, serializer):
        poem_id = self.kwargs['poem_id']
        poem = get_object_or_404(Poem, id=poem_id, is_deleted=False, is_draft=False)

        if not poem.is_visible_to(self.request.user):
            from rest_framework.exceptions import NotFound
            raise NotFound('Goşgy tapylmady.')

        if poem.author.is_banned:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied('Bu şiire yorum yapılamaz.')

        comment = serializer.save(user=self.request.user, poem=poem)

        # ✅ F() ile artır
        Poem.objects.filter(pk=poem.pk).update(comment_count=F('comment_count') + 1)

        update_poet_score(poem.author, settings.SCORE_PER_COMMENT)
        send_notification(poem.author, self.request.user, 'comment', poem=poem)

        return comment

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = self.perform_create(serializer)
        output = CommentSerializer(comment, context={'request': request})
        return Response(output.data, status=status.HTTP_201_CREATED)


# ─── YORUM GÜNCELLE / SİL ────────────────────────────────────────────────────

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/comments/<id>/
    PATCH  /api/comments/<id>/
    DELETE /api/comments/<id>/
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return CommentUpdateSerializer
        return CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            is_deleted=False
        ).select_related('user', 'user__poet_profile')

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [IsAuthenticatedOrReadOnly()]

    @transaction.atomic
    def perform_destroy(self, instance):
        poem = instance.poem

        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        instance.save(update_fields=['is_deleted', 'deleted_at'])

        # ✅ F() ile azalt, 0'ın altına düşme
        Poem.objects.filter(pk=poem.pk).update(
            comment_count=Case(
                When(comment_count__gt=0, then=F('comment_count') - 1),
                default=Value(0),
            )
        )

        CommentLike.objects.filter(comment=instance).delete()
        update_poet_score(poem.author, -settings.SCORE_PER_COMMENT)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        self.perform_destroy(instance)
        return Response({'message': 'Yorum silindi.'}, status=status.HTTP_200_OK)


# ─── YORUM BEĞENİ TOGGLE ─────────────────────────────────────────────────────

class CommentLikeToggleView(APIView):
    """
    POST /api/comments/<comment_id>/like/
    """
    permission_classes = [IsAuthenticated, IsNotBanned]

    @transaction.atomic
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, is_deleted=False)

        like, created = CommentLike.objects.get_or_create(
            user=request.user,
            comment=comment,
        )

        if created:
            # ✅ F() ile artır
            Comment.objects.filter(pk=comment.pk).update(like_count=F('like_count') + 1)
            comment.refresh_from_db()
            return Response(
                {'liked': True, 'like_count': comment.like_count},
                status=status.HTTP_201_CREATED
            )
        else:
            like.delete()
            # ✅ F() ile azalt
            Comment.objects.filter(pk=comment.pk).update(
                like_count=Case(
                    When(like_count__gt=0, then=F('like_count') - 1),
                    default=Value(0),
                )
            )
            comment.refresh_from_db()
            return Response(
                {'liked': False, 'like_count': comment.like_count},
                status=status.HTTP_200_OK
            )


# ─── ŞİİR ETKİLEŞİM İSTATİSTİKLERİ ─────────────────────────────────────────

class PoemInteractionStatsView(APIView):
    """
    GET /api/poems/<poem_id>/stats/
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, poem_id):
        poem = get_object_or_404(
            Poem,
            id=poem_id,
            is_deleted=False,
            is_draft=False,
        )

        if not poem.is_visible_to(request.user):
            from rest_framework.exceptions import NotFound
            raise NotFound('Goşgy tapylmady.')

        user_has_liked = False
        if request.user.is_authenticated:
            user_has_liked = PoemLike.objects.filter(
                user=request.user,
                poem=poem
            ).exists()

        data = {
            'poem_id': poem.id,
            'like_count': poem.like_count,
            'comment_count': poem.comment_count,
            'view_count': poem.view_count,
            'user_has_liked': user_has_liked,
        }

        serializer = PoemInteractionStatsSerializer(data)
        return Response(serializer.data)