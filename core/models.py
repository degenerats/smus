# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Speciality(models.Model):
    GROUP_TYPES = (
        ('bachelor', u'Бакалавр'),
        ('magister', u'Магистр'),
    )
    name = models.CharField(u'название', max_length=225)
    acronym = models.CharField(u'аббревиатура', max_length=100)
    speciality_type = models.CharField(u'тип обучения', choices=GROUP_TYPES, max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'специальность'
        verbose_name_plural = u'специальности'


class StudentGroup(models.Model):

    speciality = models.ForeignKey(Speciality, verbose_name=u'специальность')
    index = models.PositiveSmallIntegerField(u'индекс')
    start_year = models.PositiveIntegerField(u'год поступления')

    @property
    def name(self):
        return u'%s-%s%s' % (self.speciality.acronym, self.index, self.course)

    @property
    def course(self):
        return 1

    def __unicode__(self):
        return u'%s-%s' % (self.name, self.course)

    class Meta:
        verbose_name = u'группа'
        verbose_name_plural = u'группы'


class Student(models.Model):
    group = models.ForeignKey(StudentGroup, verbose_name='группа', related_name='students')
    last_name = models.CharField(u'фамилия', max_length=100)
    first_name = models.CharField(u'имя', max_length=100)
    middle_name = models.CharField(u'отчество', max_length=100, default='', blank=True)

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = u'студент'
        verbose_name_plural = u'студенты'


class Staff(models.Model):
    last_name = models.CharField(u'фамилия', max_length=100)
    first_name = models.CharField(u'имя', max_length=100)
    middle_name = models.CharField(u'отчество', max_length=100, default='', blank=True)
    position = models.CharField(u'должность', max_length=100, default='', blank=True)

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = u'преподаватель'
        verbose_name_plural = u'преподаватели'


class Subject(models.Model):
    SUBJECT_TYPES = (
        ('exam', u'Экзамен'),
        ('credit', u'Зачёт'),
    )

    name = models.CharField(u'название', max_length=100)
    subject_type = models.CharField(u'тип экзамена', choices=SUBJECT_TYPES, max_length=20)
    staff = models.ForeignKey(Staff, verbose_name='преподаватель')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'дисциплина'
        verbose_name_plural = u'дисциплины'