
from django.db import models

# Create your models here.

class UserData(models.Model):
    fullname = models.CharField('FULL NAME', max_length=100)
    emailid = models.EmailField('EMAIL ID', max_length=100)
    contact = models.IntegerField('Contact Number')
    address = models.CharField('Address', max_length=200)
    username = models.CharField('Username', max_length=100)
    password = models.CharField('Password', max_length=20)