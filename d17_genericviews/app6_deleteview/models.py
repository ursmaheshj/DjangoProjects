from django.db import models

# Create your models here.
class Dstudent(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name