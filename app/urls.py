from django.urls import path 
from . import views

urlpatterns = [
    path("student-lc", views.StudentAttendanceLC.as_view(), name = "student-lc"),
    path("teacher-lc", views.TeacherAttendance.as_view(), name="teacher-lc")
]
