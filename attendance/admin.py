from django.contrib import admin

# Register your models here.
from models import Attendance, Lesson


class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0
    readonly_fields = ['student']
    can_delete = False



class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'group', 'date']
    inlines = AttendanceInline,


admin.site.register(Lesson, LessonAdmin)