# Generated by Django 3.1.6 on 2021-04-09 22:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('desarrollo', '0011_auto_20210409_1833'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='desarrollo_proyecto_tareas',
            new_name='desarrollo_tareas_proyecto_tareas',
        ),
        migrations.AlterModelOptions(
            name='desarrollo_tareas_proyecto_tareas',
            options={'verbose_name': 'Tarea_por_Proy', 'verbose_name_plural': 'Tareas_por_Proy'},
        ),
    ]
