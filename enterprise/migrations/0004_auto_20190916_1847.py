# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-16 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0003_auto_20190909_2107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companies',
            new_name='Company',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Companies',
        ),
        migrations.AddField(
            model_name='employee',
            name='Company',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='enterprise.Company'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.Address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
