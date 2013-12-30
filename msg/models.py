from django.db import models

class Book(models.Model):
    first_name = models.CharField(max_length=20)
    price = models.IntegerField(max_length=10)
