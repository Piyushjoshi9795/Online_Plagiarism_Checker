from django.contrib import admin
from .models import GiveAssignment, UploadAssignment


class UploadAssignmentInline(admin.TabularInline):
    model = UploadAssignment


class AssignmentAdmin(admin.ModelAdmin):
    inlines = [
        UploadAssignmentInline,
    ]
    list_display = ("title", "subject", "date", "deadline")


admin.site.register(GiveAssignment, AssignmentAdmin, )


@admin.register(UploadAssignment)
class UploadedAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'uploaded_date']