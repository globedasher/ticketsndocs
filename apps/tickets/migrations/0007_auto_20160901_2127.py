# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-01 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20160901_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='pic_of_issue',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='ticket',
            name='url_of_issue',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
