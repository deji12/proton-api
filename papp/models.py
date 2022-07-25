from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, max_length=225, null=True, blank=True)
    REQUIRED_FIELDS =  ['username','first_name', 'last_name']
    USERNAME_FIELD = 'email'


    def get_username(self):
        return self.email

class Note(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    hobby = models.TextField()

    def __str__(self):
        return str(self.person)

class GeneratePassword(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    password_val = models.CharField(max_length=225)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.person)

class DeveloperMode(models.Model):
    name = models.CharField(max_length=225, default='name')
    file = models.URLField()

    def __str__(self):
        return self.name