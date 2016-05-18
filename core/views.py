from django.views.generic import DetailView

from models import StudentGroup


class GroupView(DetailView):
    model = StudentGroup
    template_name = 'group/view.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        semester = self.object.current_semester
        context['data'] = self.object.get_table_data(semester)
        return context
