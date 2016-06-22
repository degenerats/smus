# -*- coding:utf-8 -*-
import xlwt

from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.template.defaultfilters import date

from core.models import StudentGroup, Speciality, Staff, Student, Subject
from attendance.views import AttendanceMixin
from progress.views import ProgressMixin
from thesis.views import ThesisMixin
from core.views import MainMixin


class StaffView(DetailView):
    model = Staff
    template_name = 'staff/view.html'


class StudentView(DetailView):
    model = Student
    template_name = 'student/view.html'


class AttendanceExport(AttendanceMixin, MainMixin, DetailView):
    model = StudentGroup

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        wb = xlwt.Workbook()
        ws = wb.add_sheet(u'Успеваемость группы')
        attendance_data = context['attendance_data']

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


        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename=%s.xls' % 'attendance'
        wb.save(response)
        return response