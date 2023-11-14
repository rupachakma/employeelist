from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.TextField()
    phone_no = models.IntegerField()
    image = models.ImageField(upload_to="img",blank=True,null=True)

def __str__(self):
    return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img', blank=True, null=True)
