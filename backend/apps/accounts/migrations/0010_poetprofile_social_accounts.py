# Generated manually (Django not available in this environment)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='poetprofile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='poetprofile',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='poetprofile',
            name='imo',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='poetprofile',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='poetprofile',
            name='link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='poetprofile',
            name='tiktok',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

