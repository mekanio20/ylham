from rest_framework import serializers
from django.utils.text import slugify
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    poem_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'poem_count', 'created_at')
        read_only_fields = ('id', 'slug', 'created_at')

    def validate_name(self, value):
        qs = Category.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Bu kategori adı zaten mevcut.')
        return value

    def validate_slug(self, value):
        qs = Category.objects.filter(slug=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Bu slug zaten kullanılıyor.')
        return value

    def create(self, validated_data):
        # Slug otomatik üret
        validated_data['slug'] = slugify(validated_data['name'], allow_unicode=True)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # İsim değiştiyse slug'ı da güncelle
        if 'name' in validated_data and validated_data['name'] != instance.name:
            validated_data['slug'] = slugify(validated_data['name'], allow_unicode=True)
        return super().update(instance, validated_data)