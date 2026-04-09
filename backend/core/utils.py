from django.db.models import F
from PIL import Image
from django.core.exceptions import ValidationError
import io
import os


def update_poet_score(user, points: int):
    """
    Şairin toplam puanını günceller.
    Pozitif veya negatif değer gönderilebilir.
    Örnek: update_poet_score(user, +3)  → beğeni
           update_poet_score(user, -3)  → beğeni geri alındı
    """
    from apps.accounts.models import PoetProfile
    PoetProfile.objects.filter(user=user).update(
        total_score=F('total_score') + points
    )


def validate_image_file(file):
    """
    Resim dosyasını doğrular:
    - Maksimum boyut
    - Desteklenen format (jpg, png, jpeg)
    """
    max_size_mb = 5
    allowed_extensions = ['jpg', 'jpeg', 'png']

    # Boyut kontrolü
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f'Resim boyutu maksimum {max_size_mb}MB olabilir.')

    # Format kontrolü
    ext = os.path.splitext(file.name)[1].lower().strip('.')
    if ext not in allowed_extensions:
        raise ValidationError(f'Desteklenen formatlar: {", ".join(allowed_extensions)}')

    return file


def validate_background_image(file):
    """Şiir arka plan resmi — max 3MB."""
    max_size_mb = 3
    allowed_extensions = ['jpg', 'jpeg', 'png']

    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f'Arka plan resmi maksimum {max_size_mb}MB olabilir.')

    ext = os.path.splitext(file.name)[1].lower().strip('.')
    if ext not in allowed_extensions:
        raise ValidationError(f'Desteklenen formatlar: {", ".join(allowed_extensions)}')

    return file


def optimize_image(image_file, max_width=800, max_height=800, quality=85):
    """
    Yüklenen resmi optimize eder (boyutlandırır ve sıkıştırır).
    Orijinal dosyayı değiştirmeden yeni bir BytesIO döndürür.
    """
    img = Image.open(image_file)

    # RGBA → RGB dönüşümü (JPEG için gerekli)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    # Boyutlandır
    img.thumbnail((max_width, max_height), Image.LANCZOS)

    output = io.BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)

    return output


def create_thumbnail(image_file, size=(150, 150)):
    """Avatar için küçük thumbnail oluşturur."""
    img = Image.open(image_file)

    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    img.thumbnail(size, Image.LANCZOS)

    output = io.BytesIO()
    img.save(output, format='JPEG', quality=80)
    output.seek(0)

    return output