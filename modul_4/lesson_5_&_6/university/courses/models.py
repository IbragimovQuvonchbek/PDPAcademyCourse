from django.db import models


# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    start_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)
    speciality = models.ManyToManyField(Speciality)

    def __str__(self):
        return self.name
