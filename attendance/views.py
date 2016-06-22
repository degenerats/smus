# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.template.defaultfilters import date

from models import Attendance


class AttendanceMixin(object):
    def get_attendance_data(self, semester, subject, dates):
        if semester is None:
            semester = self.object.current_semester
            if semester is None:
                return []

        data = {}
        students = self.object.students.all()
        if subject is None:
            subjects = self.object.get_subjects(semester)
        else:
            subjects = self.object.get_subjects(semester, [subject])
        students_data = []
        for student in students:
            subjects_data = []
            attendance_all_subjects = 0
            for subject in subjects:
                attendance = []

                dates_query = {}
                if dates[0]:
                    dates_query['date__gte'] = dates[0]
                if dates[1]:
                    dates_query['date__lte'] = dates[1]
                lessons = subject.lessons.filter(**dates_query)
                attendance_count = 0
                for lesson in lessons:
                    a, created = Attendance.objects.get_or_create(
                        lesson=lesson,
                        student=student
                    )
                    attendance.append({
                        'lesson': lesson,
                        'attended': a.attended
                    })
                    if a.attended:
                        attendance_count += 1

                attendance_value = int(attendance_count*100.0/lessons.count()) if lessons.count() else 0
                subjects_data.append({
                    'subject': subject,
                    'attendance': attendance,
                    'attendance_overall': attendance_value,
                })
                attendance_all_subjects += attendance_value
            students_data.append({
                'student': student,
                'subjects': subjects_data,
                'attendance_all_subjects': int(attendance_all_subjects/subjects.count()) if subjects.count() else 0
            })

        subjects_data_full = []
        for subject in subjects:
            if dates[0]:
                dates_query['date__gte'] = dates[0]
            if dates[1]:
                dates_query['date__lte'] = dates[1]
            lessons = subject.lessons.filter(**dates_query)
            subjects_data_full.append({
                'subject': subject,
                'lessons': lessons
            })

        data['students'] = students_data
        data['subjects'] = subjects_data_full
        return data

    def write_xls(self, workbook):
        ws = workbook.add_sheet(u'Посещаемость группы')
        attendance_data = self.get_attendance_data(self.semester, self.subject, self.dates)

        ws.write_merge(0, 1, 0, 0, u'ФИО студента/ Дисциплина')
        ws.write_merge(0, 1, 1, 1, u'%')
        ws.col(0).width = 400 * 20
        ws.col(1).width = 50 * 20
        thead_i = 1
        for subject in attendance_data['subjects']:
            length = subject['lessons'].all().count()+1
            ws.write_merge(0, 0, thead_i+1, thead_i+length, subject['subject'].subject.name)

            thead_i_2 = thead_i+1
            for lesson in subject['lessons']:
                ws.write(1, thead_i_2, date(lesson.date, 'd.m.Y'))
                ws.col(thead_i_2).width = 200 * 20
                thead_i_2 += 1
            ws.write(1, thead_i_2, '%')
            ws.col(thead_i_2).width = 50 * 20

            thead_i += length

        students_i = 2
        for student in attendance_data['students']:
            ws.write(students_i, 0, student['student'].first_name)
            ws.write(students_i, 1, student['attendance_all_subjects'])
            students_i_2 = 2
            for subject in student['subjects']:
                for lesson in subject['attendance']:
                    if not lesson['attended']:
                        ws.write(students_i, students_i_2, u'н')
                    students_i_2 += 1
                ws.write(students_i, students_i_2, subject['attendance_overall'])
                students_i_2 += 1
        return workbook

    def get_context_data(self, **kwargs):
        context = super(AttendanceMixin, self).get_context_data(**kwargs)
        context['attendance_data'] = self.get_attendance_data(self.semester, self.subject, self.dates)
        return context
