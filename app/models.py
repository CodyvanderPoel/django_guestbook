from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.TextField()
    note = models.TextField()

    def __str__(self):
        return self.name
