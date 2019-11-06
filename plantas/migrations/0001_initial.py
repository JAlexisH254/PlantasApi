# Generated by Django 2.2.7 on 2019-11-06 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cultivo', models.TextField(blank=True, null=True)),
                ('guia_cultivo', models.TextField(blank=True, null=True)),
                ('imagen_cultivo', models.ImageField(upload_to='')),
                ('factor_cultivo', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_enfermedad', models.TextField(blank=True, null=True)),
                ('causa_enfermedad', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prevencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_prevencion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tratamiento1_tratamiento', models.TextField(blank=True, null=True)),
                ('tratamiento2_tratamiento', models.TextField(blank=True, null=True)),
                ('tratamiento3_tratamiento', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.TextField(blank=True, null=True)),
                ('correo_usuario', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono_usuario', models.TextField(blank=True, null=True)),
                ('contrasenia_usuario', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_insumo', models.TextField(blank=True, null=True)),
                ('id_cultivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Cultivo')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_enfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Enfermedad')),
                ('id_prevencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Prevencion')),
                ('id_tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Tratamiento')),
            ],
        ),
        migrations.AddField(
            model_name='cultivo',
            name='id_enfermedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Enfermedad'),
        ),
    ]
