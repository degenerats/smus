# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160518_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('acronym', models.CharField(max_length=100, verbose_name='\u0430\u0431\u0431\u0440\u0435\u0432\u0438\u0430\u0442\u0443\u0440\u0430')),
            ],
            options={
                'verbose_name': '\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.RemoveField(
            model_name='studentgroup',
            name='name',
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='index',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u0438\u043d\u0434\u0435\u043a\u0441'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='core.StudentGroup', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430'),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='speciality',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Speciality', verbose_name='\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c'),
            preserve_default=False,
        ),
    ]
