from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()
    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    empno = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    salary = models.IntegerField()
    join_date = models.DateField()
    def __str__(self) -> str:
        return self.name
