# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160519_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='subjects',
        ),
        migrations.AlterField(
            model_name='semestersubject',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='core.Semester'),
        ),
    ]
