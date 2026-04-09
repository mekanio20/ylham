from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='background_image',
            field=models.CharField(
                choices=[
                    ('none', 'None'),
                    ('sunset', 'Sunset'),
                    ('mountains', 'Mountains'),
                    ('forest', 'Forest'),
                    ('ocean', 'Ocean'),
                    ('city_lights', 'City Lights'),
                    ('night_sky', 'Night Sky'),
                ],
                default='none',
                max_length=50,
                verbose_name='Arka Plan Teması',
            ),
        ),
        migrations.AddField(
            model_name='poem',
            name='comment_permission',
            field=models.BooleanField(default=True, verbose_name='Yorum İzni'),
        ),
        migrations.AddField(
            model_name='poem',
            name='poem_note',
            field=models.TextField(blank=True, default='', verbose_name='Şiir Notu'),
        ),
        migrations.AddField(
            model_name='poem',
            name='public_status',
            field=models.CharField(
                choices=[
                    ('public', 'Public'),
                    ('floowers', 'Floowers'),
                    ('private', 'Private'),
                ],
                default='public',
                max_length=20,
                verbose_name='Görünürlük',
            ),
        ),
    ]
