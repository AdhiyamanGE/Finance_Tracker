from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")


class Income(models.Model):
    catg = models.CharField(max_length=100)
    amt = models.BigIntegerField()
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(models.Model):
    cag = models.CharField(max_length=100)
    amnt = models.BigIntegerField()
    daet = models.DateField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


class Reminder(models.Model):
    catg = models.CharField(max_length=100)
    amt = models.BigIntegerField()
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
