# Generated by Django 3.1.6 on 2021-04-09 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollo', '0006_remove_desarrollo_code_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='desarrollo',
            name='code_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]