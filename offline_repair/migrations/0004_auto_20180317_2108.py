# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-17 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offline_repair', '0003_computer_computer_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='technician',
            name='technician_account',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='technician',
            name='technician_password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]