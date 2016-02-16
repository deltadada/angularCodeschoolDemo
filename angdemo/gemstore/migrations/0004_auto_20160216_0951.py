# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemstore', '0003_auto_20160216_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='gemimgs',
            name='imgTypeChar',
            field=models.CharField(choices=[('A', 'FULL'), ('B', 'THUMB')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gemimgs',
            name='imgType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gemstore.GemImgTypes'),
        ),
    ]