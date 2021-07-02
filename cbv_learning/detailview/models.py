from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)


    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn  = models.CharField(max_length=100)
    count = models.IntegerField(null=True,default=0)
    