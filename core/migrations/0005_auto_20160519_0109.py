# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160519_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='\u043d\u0430\u0447\u0430\u043b\u043e \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u0430')),
                ('end', models.DateField(verbose_name='\u043a\u043e\u043d\u0435\u0446 \u0441\u0435\u043c\u0435\u0441\u0442\u0440\u0430')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.StudentGroup', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430')),
            ],
            options={
                'verbose_name': '\u0441\u0435\u043c\u0435\u0441\u0442\u0440',
                'verbose_name_plural': '\u0441\u0435\u043c\u0435\u0441\u0442\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='SemesterSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_type', models.CharField(choices=[('exam', '\u042d\u043a\u0437\u0430\u043c\u0435\u043d'), ('credit', '\u0417\u0430\u0447\u0451\u0442')], max_length=20, verbose_name='\u0442\u0438\u043f \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0430')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Semester')),
            ],
            options={
                'verbose_name': '\u044d\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u044d\u043a\u0437\u0430\u043c\u0435\u043d\u044b',
            },
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_type',
        ),
        migrations.AddField(
            model_name='semestersubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subject', verbose_name='\u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0430'),
        ),
        migrations.AddField(
            model_name='semester',
            name='subjects',
            field=models.ManyToManyField(through='core.SemesterSubject', to='core.Subject', verbose_name='\u044d\u043a\u0437\u0430\u043c\u0435\u043d\u044b'),
        ),
    ]