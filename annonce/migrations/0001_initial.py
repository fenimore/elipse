# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import annonce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donne',
            fields=[
                ('id', models.CharField(default=annonce.models.pkgen, unique=True, serialize=False, primary_key=True, max_length=6)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='pub date')),
                ('myzip', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pics', null=True)),
                ('status', models.BooleanField(default=True)),
                ('quality', models.CharField(max_length=9)),
                ('mytype', models.CharField(max_length=10)),
                ('pseudo_email', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exchice',
            fields=[
                ('id', models.CharField(default=annonce.models.pkgen, unique=True, serialize=False, primary_key=True, max_length=6)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('myzip', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pics', null=True)),
                ('status', models.BooleanField(default=True)),
                ('quality', models.CharField(max_length=9)),
                ('duration', models.CharField(max_length=9)),
                ('mytype', models.CharField(max_length=10)),
                ('pseudo_email', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.CharField(default=annonce.models.pkgen, unique=True, serialize=False, primary_key=True, max_length=6)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('myzip', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pics', null=True)),
                ('status', models.BooleanField(default=True)),
                ('quality', models.CharField(max_length=9)),
                ('mytype', models.CharField(max_length=10)),
                ('pseudo_email', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
