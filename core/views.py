# -*- coding:utf-8 -*-

from django.views.generic import DetailView, ListView
from django.http import Http404

from models import StudentGroup, Speciality, Staff, Student, Subject
from attendance.views import AttendanceMixin
from progress.views import ProgressMixin
from thesis.views import ThesisMixin


class StaffView(DetailView):
    model = Staff
    template_name = 'staff/view.html'


class StudentView(DetailView):
    model = Student
    template_name = 'student/view.html'


class GroupView(AttendanceMixin, ProgressMixin, ThesisMixin, DetailView):
    model = StudentGroup
    template_name = 'group/view.html'
    semester = None
    subject = None
    dates = None

    def get_object(self, queryset=None):
        obj = super(GroupView, self).get_object(queryset)
        self.object = obj
        self.group = obj
        self.semester = self.get_semester()
        self.subject = self.get_subject()
        self.dates = self.get_dates()
        return obj

    def get_semester(self):
        semester_number = self.request.GET.get('semester', None)
        if semester_number is not None:
            semester_number = int(semester_number)
        semester = self.object.get_semester(semester_number)
        if semester is None:
            raise Http404
        return semester

    def get_subject(self):
        subject_id = self.request.GET.get('subject', None)
        subject = None
        if subject_id is not None:
            try:
                subject = Subject.objects.get(id=subject_id)
            except Subject.DoesNotExist:
                raise Http404
            if not self.semester.subjects.filter(subject=subject):
                raise Http404
        return subject

    def get_dates(self):
        lessons_from = self.request.GET.get('from_date', None)
        lessons_to = self.request.GET.get('to_date', None)
        return lessons_from, lessons_to

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        print self.dates
        context['semesters_list'] = [
            {'semester': s,
             'number': s.number
             } for s in self.object.semesters.all()
        ]
        context['subjects_list'] = [
            {'name': s.subject.name,
             'id': s.subject.id
             } for s in self.semester.subjects.all()
            ]
        context['current_semester'] = self.semester
        context['current_subject'] = self.subject
        context['current_dates'] = self.dates
        return context


class SpecialityView(ListView):
    model = Speciality
    template_name = 'speciality/view.html'

    def get_context_data(self, **kwargs):
        context = super(SpecialityView, self).get_context_data(**kwargs)
        context['speciality_type'] = u'Бакалавриат' if self.kwargs['level'] == 'bachelor' else u'Магистратура'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super(SpecialityView, self).get_queryset(*args, **kwargs)
        queryset = queryset.filter(speciality_type=self.kwargs['level'])
        return queryset
