from django.shortcuts import render

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

    def get_context_data(self, **kwargs):
        context = super(AttendanceMixin, self).get_context_data(**kwargs)
        context['attendance_data'] = self.get_attendance_data(self.semester, self.subject, self.dates)
        return context
