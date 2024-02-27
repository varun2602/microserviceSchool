from django.db import models


class StudentAttendance(models.Model):
    name = models.CharField(max_length = 50, blank = True, null = True)
    attendance = models.IntegerField()

    def __str__(self):
        return self.name 
    

class TeacherAttendance(models.Model):
    name = models.CharField(max_length = 50, blank = True, null = True)
    attendance = models.IntegerField()

    def __str__(self):
        return self.name
