# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160519_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='group_type',
        ),
        migrations.AddField(
            model_name='speciality',
            name='speciality_type',
            field=models.CharField(choices=[('bachelor', '\u0411\u0430\u043a\u0430\u043b\u0430\u0432\u0440'), ('magister', '\u041c\u0430\u0433\u0438\u0441\u0442\u0440')], default='bachelor', max_length=20, verbose_name='\u0442\u0438\u043f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]
