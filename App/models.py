from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=35)

    class Meta:
        db_table = 'user'


class Address(models.Model):
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)

    class Meta:
        db_table = 'address'
