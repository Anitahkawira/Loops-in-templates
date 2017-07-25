from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.CharField(max_length = 20)
    coarse = models.CharField(max_length = 20)
    Description = models.CharField(max_length = 20)
    def __str__ (self):
        return self.names
