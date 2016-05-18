# -*- coding:utf-8 -*-
from django.contrib import admin

from models import *


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


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


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGroup, StudentGroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Speciality, SpecialityAdmin)