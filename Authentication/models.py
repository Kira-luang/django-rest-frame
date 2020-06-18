from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=225)
    is_super = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'
