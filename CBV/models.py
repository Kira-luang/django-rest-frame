from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=155)
    price = models.IntegerField()

    class Meta:
        db_table = 'book'

    def get_dict(self):
        return {'name': self.name , 'price': self.price}
