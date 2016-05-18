# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StudentGroup(models.Model):
    GROUP_TYPES = (
        ('bachelor', u'Бакалавр'),
        ('magister', u'Магистр'),
    )

    name = models.CharField(u'название', max_length=100)
    start_year = models.PositiveIntegerField(u'год поступления')
    group_type = models.CharField(u'тип обучения', choices=GROUP_TYPES, max_length=20)

    @property
    def course(self):
        return 1

    class Meta:
        verbose_name = u'группа'
        verbose_name_plural = u'группы'


class Student(models.Model):
    group = models.ForeignKey(StudentGroup, verbose_name='группа')
    last_name = models.CharField(u'фамилия', max_length=100)
    first_name = models.CharField(u'имя', max_length=100)
    middle_name = models.CharField(u'отчество', max_length=100)

    @property
    def full_name(self):
        return u'%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = u'студент'
        verbose_name_plural = u'студенты'