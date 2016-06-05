from django.shortcuts import render

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

    def get_context_data(self, **kwargs):
        context = super(ProgressMixin, self).get_context_data(**kwargs)
        context['progress_data'] = self.get_progress_data(self.semester)
        return context
