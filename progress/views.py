# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.template.defaultfilters import date

from models import Progress

class ProgressMixin(object):
    def get_progress_data(self, semester):
        if semester is None:
            semester = self.object.current_semester
            if semester is None:
                return []

        data = {}
        students = self.object.students.all()
        subjects = self.object.get_subjects(semester).order_by('subject_type')
        students_data = []
        for student in students:
            subjects_data = []
            for subject in subjects:
                subjects_data.append({
                    'subject': subject,
                    'progress': student.get_progress(subject)
                })
            students_data.append({
                'student': student,
                'subjects': subjects_data,
                'progress_overall': student.get_total_progress()
            })

        subjects_data_full = {
            'exam': [],
            'credit': [],
        }
        for subject in subjects:
            if subject.subject_type == 'exam':
                subjects_data_full['exam'].append(subject)
            if subject.subject_type == 'credit':
                subjects_data_full['credit'].append(subject)

        data['students'] = students_data
        data['subjects'] = subjects_data_full
        return data

    def write_xls(self, workbook):
        ws = workbook.add_sheet(u'Успеваемость группы')
        progress_data = self.get_progress_data(self.semester)

        ws.write_merge(0, 1, 0, 0, u'ФИО студента')
        ws.write_merge(0, 1, 1, 1, u'Средний балл')
        ws.col(0).width = 250 * 20
        ws.col(1).width = 200 * 20
        thead_i = 1
        for kind in ['credit', 'exam']:
            length = len(progress_data['subjects'][kind])
            ws.write_merge(0, 0, thead_i+1, thead_i+length, u'Экзамены' if kind == 'exam' else u'Зачёты')

            thead_i_2 = thead_i+1
            for subject in progress_data['subjects'][kind]:
                ws.write(1, thead_i_2, subject.subject.name)
                ws.col(thead_i_2).width = 300 * 20
                thead_i_2 += 1

            thead_i += length

        students_i = 2
        for student in progress_data['students']:
            ws.write(students_i, 0, student['student'].first_name)
            ws.write(students_i, 1, student['progress_overall'])
            students_i_2 = 2

            if not progress_data['subjects']['credit']:
                students_i_2 += 1
            for subject in student['subjects']:
                ws.write(students_i, students_i_2, subject['progress'])
                students_i_2 += 1
        return workbook


    def get_context_data(self, **kwargs):
        context = super(ProgressMixin, self).get_context_data(**kwargs)
        context['progress_data'] = self.get_progress_data(self.semester)
        return context
