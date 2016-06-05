from django.shortcuts import render

from models import Thesis


class ThesisMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ThesisMixin, self).get_context_data(**kwargs)
        context['thesis_data'] = self.semester.thesis_set.all()
        return context