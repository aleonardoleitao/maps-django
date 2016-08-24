# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-21 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_ordem_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='maps',
            name='data_edicao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maps',
            name='data_finalizacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maps',
            name='user_edicao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='maps',
            name='user_finalizacao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='file',
            field=models.FileField(blank=True, upload_to=b'/Users/andrel/Desenvolvimento/Pessoal/grg/maps-django/localidades/media'),
        ),
    ]
