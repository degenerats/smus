# -*- coding:utf-8 -*-
from django.db import models

from core.models import SemesterSubject, Student, StudentGroup


class Attendance(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'студент')
    attended = models.BooleanField(u'присутствовал', default=False)
    lesson = models.ForeignKey('Lesson', verbose_name=u'занятие')

    def __unicode__(self):
        return u'%s, %s, %s' % (self.student, self.lesson.semester_subject, self.lesson.date)

    class Meta:
        verbose_name = u'посещение'
        verbose_name_plural = u'посещения'


class Lesson(models.Model):
    semester_subject = models.ForeignKey(SemesterSubject, verbose_name=u'предмет', related_name='lessons')
    date = models.DateField(verbose_name=u'дата')

    def __unicode__(self):
        return u'%s, %s' % (self.semester_subject, self.date)

    def save(self, *args, **kwargs):
        super(Lesson, self).save(*args, **kwargs)
        for student in self.semester_subject.semester.group.students.all():
            Attendance.objects.get_or_create(
                student=student,
                lesson=self
            )

    class Meta:
        verbose_name = u'занятие'
        verbose_name_plural = u'занятия'