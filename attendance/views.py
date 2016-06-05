from django.shortcuts import render


class AttendanceMixin(object):
    def get_context_data(self, **kwargs):
        context = super(AttendanceMixin, self).get_context_data(**kwargs)
        context['attendance_data'] = self.object.get_table_data(self.semester, self.subject, self.dates)
        return context
