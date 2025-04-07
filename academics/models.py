from django.contrib.auth.models import User
from django.db import models

class StudentProfile(models.Model):
    # name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.roll_number}"

class MSEMark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.FloatField()
    exam_type = models.CharField(max_length=10, choices=[('MSE1', 'MSE 1'), ('MSE2', 'MSE 2')])

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject} ({self.exam_type})"
