# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GemImgs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(default='image_not_avail.png', max_length=2000)),
                ('imgTypeChar', models.CharField(choices=[('A', 'FULL'), ('B', 'THUMB')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GemImgTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imgType', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('description', models.CharField(blank=True, max_length=1056, null=True)),
                ('canPurchase', models.BooleanField(default=False)),
                ('soldOut', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stars', models.SmallIntegerField(default=1)),
                ('body', models.CharField(default='...', max_length=800)),
                ('author', models.CharField(default='george@internet.com', max_length=254)),
                ('gem', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems')),
            ],
        ),
        migrations.AddField(
            model_name='gemimgs',
            name='gem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems'),
        ),
        migrations.AddField(
            model_name='gemimgs',
            name='imgType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gemstore.GemImgTypes'),
        ),
    ]
