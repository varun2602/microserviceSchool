from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from . import models
from .  import serializers
from . customauth import CustomAuthentication
from . permissions import IsStudent, IsTeacher 

class StudentAttendanceLC(ListCreateAPIView):
    queryset = models.StudentAttendance.objects.all()
    serializer_class = serializers.StudentAttendanceSerializer 
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsStudent]


class TeacherAttendance(ListCreateAPIView):
    queryset = models.TeacherAttendance.objects.all()
    serializer_class = serializers.TeacherAttendanceSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsTeacher]