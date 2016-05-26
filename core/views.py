# -*- coding:utf-8 -*-

from django.views.generic import DetailView, ListView

from models import StudentGroup, Speciality

class GroupView(DetailView):
    model = StudentGroup
    template_name = 'group/view.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        semester = self.object.current_semester
        context['data'] = self.object.get_table_data(semester)
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
