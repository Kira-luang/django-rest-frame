from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    sex = models.BooleanField(default=False)

    class Meta:
        db_table = 'student'


class Teacher(models.Model):
    name = models.CharField(max_length=10)
    sex = models.BooleanField(default=False)

    class Meta:
        db_table = 'teacher'
