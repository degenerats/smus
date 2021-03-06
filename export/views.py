# -*- coding:utf-8 -*-
import xlwt
from transliterate import translit

from django.views.generic import DetailView, ListView
from django.http import HttpResponse

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


class AttendanceExport(AttendanceMixin, ProgressMixin, ThesisMixin, MainMixin, DetailView):
    model = StudentGroup

    def write_xls(self):
        wb = xlwt.Workbook()
        workbook = AttendanceMixin.write_xls(self, wb)
        workbook = ProgressMixin.write_xls(self, workbook)
        workbook = ThesisMixin.write_xls(self, workbook)
        return workbook

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        wb = self.write_xls()

        filename = translit(self.object.name, 'ru', reversed=True)
        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = u'attachment; filename=%s.xls' % filename
        wb.save(response)
        return response