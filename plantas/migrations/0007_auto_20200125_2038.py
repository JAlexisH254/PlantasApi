# Generated by Django 3.0.1 on 2020-01-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0006_auto_20191221_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='afeccion',
            name='descripcion_efeccion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='afeccion',
            name='imagen_afeccion',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='afeccion',
            name='prevencion_afeccion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
