from django.contrib import admin
from . import models 

@admin.register(models.StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "attendance"]


@admin.register(models.TeacherAttendance)
class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "attendance"]