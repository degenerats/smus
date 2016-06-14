from django.shortcuts import render
from django.http import Http404

from models import Thesis


class ThesisMixin(object):
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