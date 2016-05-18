# -*- coding:utf-8 -*-
from django.contrib import admin

from models import *


class StudentInline(admin.TabularInline):
    model = Student


class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = StudentInline,


class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'group']


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGroup, StudentGroupAdmin)