from django.utils import timezone


class SoftDeleteMixin:
    """
    Modellere soft delete özelliği kazandırır.
    Model'de `is_deleted` ve `deleted_at` alanları olmalıdır.
    """

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])


class ActiveObjectsManager:
    """
    QuerySet'ten silinmiş kayıtları otomatik filtreler.
    Manager olarak kullanılır: objects = ActiveObjectsManager()
    """
    pass