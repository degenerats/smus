# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.apps import apps


class SemesterSubject(models.Model):
    EXAM_TYPES = (
        ('exam', u'Экзамен'),
        ('credit', u'Зачёт'),
    )

    semester = models.ForeignKey('Semester', related_name='subjects')
    subject = models.ForeignKey('Subject', verbose_name=u'дисциплина')
    subject_type = models.CharField(u'тип экзамена', choices=EXAM_TYPES, max_length=20)

    def __unicode__(self):
        return '%s, %s' % (self.semester, self.subject)

    class Meta:
        verbose_name = u'экзамен'
        verbose_name_plural = u'экзамены'


class Semester(models.Model):
    start = models.DateField(u'начало семестра')
    end = models.DateField(u'конец семестра')
    group = models.ForeignKey('StudentGroup', verbose_name=u'группа')

    def __unicode__(self):
        return '%s - %s, %s' % (self.start, self.end, self.group)

    class Meta:
        verbose_name = u'семестр'
        verbose_name_plural = u'семестры'


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

class Subject(models.Model):
    name = models.CharField(u'название', max_length=100)
    staff = models.ForeignKey('Staff', verbose_name='преподаватель')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'дисциплина'
        verbose_name_plural = u'дисциплины'


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

    @property
    def current_semester(self):
        current_semester = Semester.objects.filter(
            group=self,
            start__lt=datetime.datetime.now(),
            end__gt=datetime.datetime.now()
        )
        if current_semester:
            return current_semester[0]
        else:
            last_semester = Semester.objects.filter(group=self).last()
            if last_semester:
                return last_semester
            else:
                return None

    def get_subjects(self, semester):
        if semester is None:
            return []
        return semester.subjects.all()

    def get_table_data(self, semester):
        Attendance = apps.get_model('attendance', 'attendance')
        if semester is None:
            semester = self.current_semester()
            if semester is None:
                return []

        subjects = self.get_subjects(semester)
        data = []
        for subject in subjects:
            lessons = subject.lessons.all()
            students = []
            for student in self.students.all():
                attendance = []
                for lesson in lessons:
                    a, created = Attendance.objects.get_or_create(
                        lesson=lesson,
                        student=student
                    )
                    attendance.append(a.attended)

                students.append({
                    'student': student,
                    'attendance': attendance
                })
            data.append({
                'subject': subject,
                'lessons': lessons,
                'students': students
            })
        return data

    def __unicode__(self):
        return u'%s' % self.name

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
