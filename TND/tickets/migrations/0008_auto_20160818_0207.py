# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_ticket_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]