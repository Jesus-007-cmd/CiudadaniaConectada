# Generated by Django 4.2.4 on 2023-08-27 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportessolicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avancereporte',
            name='funcionario',
            field=models.CharField(max_length=20, verbose_name='id Funcionario'),
        ),
        migrations.AlterField(
            model_name='solicitudinformacion',
            name='id_ciudadano',
            field=models.CharField(max_length=20, verbose_name='id Ciudadano'),
        ),
        migrations.AlterField(
            model_name='solicitudinformacion',
            name='id_funcionario',
            field=models.CharField(max_length=20, verbose_name='id funcionario'),
        ),
    ]
