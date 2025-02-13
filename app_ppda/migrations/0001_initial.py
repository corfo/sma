# Generated by Django 5.1.6 on 2025-02-13 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('codigo', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('unidad', models.CharField(choices=[('cantidad', 'cantidad'), ('porcentaje', 'Porcentaje')], default='cantidad', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('indicador', models.CharField(max_length=100, unique=True)),
                ('formula_calculo', models.CharField(max_length=100, unique=True)),
                ('medio_verificador', models.CharField(max_length=100, unique=True)),
                ('tipo_medida', models.CharField(max_length=100, unique=True)),
                ('frecuencia', models.CharField(choices=[('unica', 'Única'), ('anual', 'Anual'), ('cada_5_anios', 'Cada 5 años')], default='unica', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedidaIndicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('periodo', models.CharField(max_length=20)),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ppda.indicador')),
                ('medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ppda.medida')),
            ],
        ),
        migrations.AddField(
            model_name='medida',
            name='indicadores',
            field=models.ManyToManyField(blank=True, related_name='medidas', through='app_ppda.MedidaIndicador', to='app_ppda.indicador'),
        ),
        migrations.CreateModel(
            name='Ppda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('comunas', models.ManyToManyField(blank=True, related_name='comunas', to='app_ppda.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='PpdaOrganismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medidas', models.ManyToManyField(blank=True, related_name='medidas', to='app_ppda.medida')),
                ('organismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ppda.organismo')),
                ('ppda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ppda.ppda')),
            ],
        ),
        migrations.AddField(
            model_name='ppda',
            name='organismos',
            field=models.ManyToManyField(blank=True, related_name='organismos', through='app_ppda.PpdaOrganismo', to='app_ppda.organismo'),
        ),
    ]
