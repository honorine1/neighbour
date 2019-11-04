from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime as dt
# from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_pic =  models.ImageField(default='default.jpg',upload_to = 'profile_pics/', blank=True) 
    bio = models.TextField(max_length = 200)
    neighbourhoodName = models.TextField(max_length = 200)
    contact  = models.IntegerField(default=None)
    general_loc = models.CharField(max_length = 50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Post(models.Model):
    
    image =  models.ImageField(upload_to = 'post_pics/', blank=True)
    desc = models.TextField(max_length=200)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc
    
class Neighbour(models.Model):
    name = models.CharField(max_length=20)
    location = models.TextField(max_length=50)
    healthCare = models.TextField(max_length=50)
    nearPolice = models.TextField(max_length=50)
    occupantsCount = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=50)
    bss_email = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Neighbour = models.ForeignKey(Neighbour,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Health(models.Model):
#     name =  models.CharField(max_length=50)
#     location =  models.CharField(max_length=50)
#     contact =  models.IntegerField(default=0)
#     neighbour = models.ForeignKey(Neighbour,on_delete=models.CASCADE)
#     admin = models.ForeignKey(Admin,on_delete=models.CASCADE)

# class Police(models.Model):
#     location = models.CharField(max_length=50)
#     neighbour = models.ForeignKey(Neighbour,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.location



