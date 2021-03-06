# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.PositiveIntegerField(default=0, verbose_name='position')),
                ('show', models.BooleanField()),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Content type',
                'ordering': ['pos', 'name'],
                'verbose_name_plural': 'Content types',
            },
        ),
    ]
