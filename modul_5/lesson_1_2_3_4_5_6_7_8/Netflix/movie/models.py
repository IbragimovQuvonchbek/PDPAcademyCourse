from django.db import models
from django.contrib.auth.models import User


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


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
