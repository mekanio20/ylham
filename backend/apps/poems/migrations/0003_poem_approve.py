from django.db import migrations, models


def set_approve_for_existing_published(apps, schema_editor):
    Poem = apps.get_model('poems', 'Poem')
    Poem.objects.filter(is_draft=False).update(approve=True)


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0002_poem_visibility_and_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='approve',
            field=models.BooleanField(
                default=False,
                help_text='Tassyklanmasa, diňe ýazyjy we admin görýär; beýleki ulanyjylar üçin görünmeýär.',
                verbose_name='Admin tassyklamasy',
            ),
        ),
        migrations.RunPython(set_approve_for_existing_published, migrations.RunPython.noop),
    ]
