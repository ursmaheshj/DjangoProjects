from django.db import models

# Create your models here.
class User(models.Model):
    student_name = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)