from email.policy import default
from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.


class Person(models.Model):
    forename = models.CharField(
        max_length=20, help_text='Forename / First Name')
    surname = models.CharField(
        max_length=30, help_text='Surname / Last Name')
    birthday = models.DateField()
    deceased = models.BooleanField(default=False)
    deathDay = models.DateField(null=True, blank=True)
    pro_pic = models.ImageField(null=True, blank=True)
    about = models.CharField(max_length=500, null=True)
    mother = models.ForeignKey('self',
                               models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='children_of_mother')
    father = models.ForeignKey('self',
                               models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='children_of_father')
    spouse = models.ForeignKey('self', models.SET_NULL,
                               blank=True, null=True, related_name='spouse_of')

    def __str__(self):
        return self.forename


class Memory(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='Memory')
    author = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='memory')

    def __str__(self):
        return self.title


class SocialPost(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    author: models.CharField()
    time: models.CharField()
    likes: models.IntegerField(default=0)

    def __str__(self):
        return self.title
