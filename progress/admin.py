from django.contrib import admin

from models import SemesterSubject, Progress


class ProgressInline(admin.TabularInline):
    model = Progress
    extra = 0
    readonly_fields = ['student']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SemesterSubjectAdmin(admin.ModelAdmin):
    list_display = ['semester', 'subject', 'subject_type']
    list_filter = ['subject_type']
    inlines = [ProgressInline]


admin.site.register(SemesterSubject, SemesterSubjectAdmin)