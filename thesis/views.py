# -*- coding:utf-8 -*-
from django.http import Http404
from django.template.defaultfilters import date

from models import Thesis


class ThesisMixin(object):
    def write_xls(self, workbook):
        ws = workbook.add_sheet(u'Курсовые работы')
        thesis_data = self.semester.thesis_set.all()

        ws.write(0, 0, u'ФИО студента')
        ws.write(0, 1, u'Тема курсовой работы')
        ws.write(0, 2, u'Научный руководитель')
        ws.write(0, 3, u'Прогресс')
        ws.write(0, 4, u'Дата обновления')
        ws.write(0, 5, u'Оценка')

        students_i = 1
        for thesis in thesis_data:
            ws.write(students_i, 0, '%s %s' % (thesis.student.last_name, thesis.student.first_name))
            ws.write(students_i, 1, thesis.topic)
            ws.write(students_i, 2, thesis.professor.__unicode__() if thesis.professor else '')
            ws.write(students_i, 3, '%s%%' % thesis.progress)
            ws.write(students_i, 4, date(thesis.last_change_date, 'd.m.Y'))
            ws.write(students_i, 5, '')
            students_i += 1

        ws.col(0).width = 500 * 20
        ws.col(1).width = 600 * 20
        ws.col(2).width = 400 * 20
        ws.col(3).width = 200 * 20
        ws.col(4).width = 200 * 20
        ws.col(5).width = 200 * 20

        if self.group.get_final_semester:
            final_thesis_data = self.group.get_final_semester.thesis_set.all()
        else:
            final_thesis_data = None

        if final_thesis_data:
            ws = workbook.add_sheet(u'Дипломные работы')
            ws.write(0, 0, u'ФИО студента')
            ws.write(0, 1, u'Тема дипломной работы')
            ws.write(0, 2, u'Научный руководитель')
            ws.write(0, 3, u'Прогресс')
            ws.write(0, 4, u'Дата обновления')
            ws.write(0, 5, u'Оценка')

            students_i = 1
            for thesis in final_thesis_data:
                ws.write(students_i, 0, '%s %s' % (thesis.student.last_name, thesis.student.first_name))
                ws.write(students_i, 1, thesis.topic)
                ws.write(students_i, 2, thesis.professor.__unicode__() if thesis.professor else '')
                ws.write(students_i, 3, '%s%%' % thesis.progress)
                ws.write(students_i, 4, date(thesis.last_change_date, 'd.m.Y'))
                ws.write(students_i, 5, '')
                students_i += 1

            ws.col(0).width = 500 * 20
            ws.col(1).width = 600 * 20
            ws.col(2).width = 400 * 20
            ws.col(3).width = 200 * 20
            ws.col(4).width = 200 * 20
            ws.col(5).width = 200 * 20
        return workbook

    def get_context_data(self, **kwargs):
        context = super(ThesisMixin, self).get_context_data(**kwargs)
        if not self.semester.is_final:
            context['thesis_data'] = self.semester.thesis_set.all()
        else:
            raise Http404

        if self.group.get_final_semester:
            context['final_thesis_data'] = self.group.get_final_semester.thesis_set.all()
        else:
            context['final_thesis_data'] = None

        return context