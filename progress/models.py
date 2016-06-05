# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import SemesterSubject, Student


class Progress(models.Model):
    MARKS = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('zachet', u'Зачёт'),
    )

    subject = models.ForeignKey(SemesterSubject, verbose_name=u'предмет')
    student = models.ForeignKey(Student, verbose_name=u'студент')
    mark = models.CharField(u'оценка', choices=MARKS, blank=True, default='', max_length=15)

    def __unicode__(self):
        return '%s, %s' % (self.subject, self.student)

    class Meta:
        verbose_name = u'Успеваемость'
        verbose_name_plural = u'Успеваемость'
