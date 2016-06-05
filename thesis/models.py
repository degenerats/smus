# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import Semester, Student, Staff


class Thesis(models.Model):
    semester = models.ForeignKey(Semester, verbose_name=u'семестр')
    student = models.ForeignKey(Student, verbose_name=u'студент')
    topic = models.TextField(u'тема', blank=True, default='')
    progress = models.PositiveIntegerField(u'прогресс', default=0)
    professor = models.ForeignKey(Staff, verbose_name=u'научный руководитель', null=True, blank=True)
    last_change_date = models.DateField(u'дата последнего изменения', null=True, blank=True)

    def __unicode__(self):
        return '%s, %s' % (self.semester, self.student)

    class Meta:
        verbose_name = u'работа'
        verbose_name_plural = u'курсовые и дипломы'
