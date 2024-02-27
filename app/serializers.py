from rest_framework import serializers 
from . import models

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAttendance 
        fields = "__all__"



class TeacherAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherAttendance
        fields = "__all__" 
