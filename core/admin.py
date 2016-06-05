# -*- coding:utf-8 -*-
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from models import *
from thesis.models import Thesis


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class SubjectInline(admin.TabularInline):
    model = SemesterSubject
    extra = 0
    readonly_fields = ['subject', 'subject_type', 'progress_edit']


class ThesisInline(admin.TabularInline):
    model = Thesis
    extra = 0
    readonly_fields = ['student', 'last_change_date']
    fields = ['student', 'topic', 'professor', 'progress', 'last_change_date']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = StudentInline,


class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'group']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'staff']


class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position']


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['name']


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['group', 'number']
    inlines = SubjectInline, ThesisInline

    def change_view(self, *args, **kwargs):
        self.readonly_fields = ('group', )
        return super(SemesterAdmin, self).change_view(*args, **kwargs)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGroup, StudentGroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(SemesterConfiguration, SingletonModelAdmin)
