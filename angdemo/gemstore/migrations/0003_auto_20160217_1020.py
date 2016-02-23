# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemstore', '0002_auto_20160217_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullDisplays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(default='assets/img/noImage.png', max_length=2000)),
                ('gem', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems')),
                ('reviews', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gemstore.Reviews')),
            ],
        ),
        migrations.CreateModel(
            name='ThumbDisplays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(default='assets/img/noImage_th.png', max_length=2000)),
                ('gem', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='gemstore.Gems')),
            ],
        ),
        migrations.RemoveField(
            model_name='gemimgs',
            name='gem',
        ),
        migrations.RemoveField(
            model_name='gemimgs',
            name='imgType',
        ),
        migrations.DeleteModel(
            name='GemImgs',
        ),
        migrations.DeleteModel(
            name='GemImgTypes',
        ),
    ]
