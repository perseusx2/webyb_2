# Generated by Django 3.1.4 on 2021-01-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210108_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='descripcion2',
            field=models.TextField(blank=True, help_text='Descripción2', max_length=400),
        ),
        migrations.AddField(
            model_name='servicio',
            name='listado',
            field=models.TextField(blank=True, help_text='Listado', max_length=1000),
        ),
    ]