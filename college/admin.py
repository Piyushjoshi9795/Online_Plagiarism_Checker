from django.contrib import admin
from .models import Subject, SubjectStudent
from assignments.models import GiveAssignment


class StudentInline(admin.TabularInline):
    model = SubjectStudent

class AssignmentInline(admin.TabularInline):
    model = GiveAssignment


class SubjectAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline, AssignmentInline
    ]
    list_display = ('subject', 'teacher', 'faculty', 'semester')
    prepopulated_fields = {'slug': ('subject',)}
    # list_filter = ('status', 'created', 'publish', 'subject')
    # search_fields = ('subject', 'teacher')
    # raw_id_fields = ('teacher',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')


admin.site.register(Subject, SubjectAdmin)
