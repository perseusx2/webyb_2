# Generated by Django 3.1.4 on 2021-01-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(help_text='Descripción', max_length=200),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='icono',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='titulo',
            field=models.CharField(help_text='Título', max_length=30),
        ),
    ]
