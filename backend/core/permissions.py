from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsNotBanned(BasePermission):
    """Yasaklı kullanıcıların erişimini engeller."""
    message = 'Hesabınız yasaklanmıştır.'

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            not request.user.is_banned
        )


class IsOwnerOrAdmin(BasePermission):
    """Sadece nesnenin sahibi veya admin erişebilir."""
    message = 'Bu işlem için yetkiniz yok.'

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        # obj.user veya obj.author alanını kontrol et
        owner = getattr(obj, 'user', None) or getattr(obj, 'author', None)
        return owner == request.user


class IsOwnerOnly(BasePermission):
    """Sadece nesnenin sahibi erişebilir, admin dahil değil."""
    message = 'Bu işlem için yetkiniz yok.'

    def has_object_permission(self, request, view, obj):
        owner = getattr(obj, 'user', None) or getattr(obj, 'author', None)
        return owner == request.user


class IsAdminOrReadOnly(BasePermission):
    """GET isteklerine herkese izin ver, yazma işlemleri sadece admin."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)