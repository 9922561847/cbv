from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length = 100)
    spass = models.CharField(max_length = 25)
    semail = models.CharField(max_length=100)


    def __str__(self):
        return self.sname