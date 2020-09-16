from django.db import models
from django.forms import ModelForm

# Create your models here.


class UserManager(models.Manager):
    def create_user(self, f_name, l_name, email, password):
        user = self.create(first_name=f_name, last_name=l_name, email=email, password=password)
        return user


class User(models.Model):
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=40, blank=False, unique=True)
    password = models.CharField(max_length=150, blank=False)

    objects = UserManager()
