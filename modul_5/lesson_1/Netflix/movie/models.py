from django.db import models


# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    imdb = models.FloatField()
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name
