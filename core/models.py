# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import datetime

from solo.models import SingletonModel

from django.db import models
from django.apps import apps


GROUP_MODE_FULL = (
    ('ochnaya', u'Очная', u'о'),
    ('zaochnaya', u'Заочная', u'з'),
)


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
    group = models.ForeignKey('StudentGroup', verbose_name=u'группа', related_name='semesters')

    def __unicode__(self):
        return '%s, %s семестр' % (self.group, self.number)

    @property
    def number(self):
        count = 1
        semesters = self.group.semesters.all().order_by('pk')
        for semester in semesters:
            if semester == self:
                return count
            else:
                count += 1

    class Meta:
        verbose_name = u'семестр'
        verbose_name_plural = u'семестры'


class Speciality(models.Model):
    GROUP_TYPES = (
        ('bachelor', u'Бакалавр'),
        ('magister', u'Магистр'),
    )
    GROUP_MODE = ((x[0], x[1]) for x in GROUP_MODE_FULL)

    name = models.CharField(u'название', max_length=225)
    acronym = models.CharField(u'аббревиатура', max_length=100)
    speciality_type = models.CharField(u'уровень обучения', choices=GROUP_TYPES, max_length=20)
    speciality_mode = models.CharField(u'вид обучения', choices=GROUP_MODE, max_length=20)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.get_speciality_mode_display().lower())

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
        mode_letter = u'о'
        for mode in GROUP_MODE_FULL:
            if mode[0] == self.speciality.speciality_mode:
                mode_letter = mode[2]
        return u'%s-%s-%s/%s' % (self.speciality.acronym, mode_letter, str(self.start_year)[-2:], self.index)

    @property
    def course(self):
        return 1

    @property
    def current_semester(self):
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

        data = {}
        students = self.students.all()
        subjects = self.get_subjects(semester)
        students_data = []
        for student in students:
            subjects_data = []
            for subject in subjects:
                attendance = []
                lessons = subject.lessons.all()
                for lesson in lessons:
                    a, created = Attendance.objects.get_or_create(
                        lesson=lesson,
                        student=student
                    )
                    print a.attended
                    print a.attended
                    attendance.append({
                        'lesson': lesson,
                        'attended': a.attended
                    })
                subjects_data.append({
                    'subject': subject,
                    'attendance': attendance
                })
            students_data.append({
                'student': student,
                'subjects': subjects_data
            })

        data['students'] = students_data
        data['subjects'] = subjects

        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data['students'])
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


class SemesterConfiguration(SingletonModel):
    first_semester_start = models.DateField(u'начало первого семестра')
    first_semester_end = models.DateField(u'конец первого семестра')
    second_semester_start = models.DateField(u'начало второго семестра')
    second_semester_end = models.DateField(u'конец второго семестра')

    class Meta:
        verbose_name = u'настройки семестров'
        verbose_name_plural = u'настройки семестров'
