# Generated by Django 3.1.6 on 2021-04-09 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollo', '0015_proyecto_tareas_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencias',
            name='proy_tarea_hijo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proy_tarea_hijo_id', to='desarrollo.proyecto_tareas'),
        ),
        migrations.AlterField(
            model_name='dependencias',
            name='proy_tarea_padre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proy_tarea_padre_id', to='desarrollo.proyecto_tareas'),
        ),
    ]
