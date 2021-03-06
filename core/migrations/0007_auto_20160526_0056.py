# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160519_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_semester_start', models.DateField(verbose_name='\u043d\u0430\u0447\u0430\u043b\u043e \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u0430')),
                ('first_semester_end', models.DateField(verbose_name='\u043a\u043e\u043d\u0435\u0446 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u0430')),
                ('second_semester_start', models.DateField(verbose_name='\u043d\u0430\u0447\u0430\u043b\u043e \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u0430')),
                ('second_semester_end', models.DateField(verbose_name='\u043a\u043e\u043d\u0435\u0446 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u0430')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u043e\u0432',
                'verbose_name_plural': '\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u043e\u0432',
            },
        ),
        migrations.RemoveField(
            model_name='semester',
            name='end',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='start',
        ),
        migrations.AddField(
            model_name='speciality',
            name='speciality_mode',
            field=models.CharField(choices=[('ochnaya', '\u041e\u0447\u043d\u0430\u044f'), ('zaochnaya', '\u0417\u0430\u043e\u0447\u043d\u0430\u044f')], default='ochnaya', max_length=20, verbose_name='\u0432\u0438\u0434 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='semester',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='core.StudentGroup', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_type',
            field=models.CharField(choices=[('bachelor', '\u0411\u0430\u043a\u0430\u043b\u0430\u0432\u0440'), ('magister', '\u041c\u0430\u0433\u0438\u0441\u0442\u0440')], max_length=20, verbose_name='\u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f'),
        ),
    ]
