# Generated by Django 4.2.4 on 2023-08-29 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportessolicitudes', '0002_alter_avancereporte_funcionario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariofuncionario',
            name='comentario',
            field=models.TextField(default='no respondido aún', verbose_name='Comentario'),
            preserve_default=False,
        ),
    ]
