# Generated by Django 3.2.9 on 2021-12-06 12:44

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('modelo', models.CharField(max_length=50, verbose_name='nome')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Móvel',
                'verbose_name_plural': 'Móveis',
            },
        ),
    ]