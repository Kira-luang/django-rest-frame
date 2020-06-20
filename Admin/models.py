from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=18)
    sex = models.BooleanField(default=False)

    class Meta:
        db_table = 'human'

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=18)
    owner = models.ForeignKey(Human , models.CASCADE)

    class Meta:
        db_table = 'pet'
