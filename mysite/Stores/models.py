from django.db import models
from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

# def upload_location(isinstance,filename):
#     filebase, extention = filename.split(".")
#     return "%s/%s/%s" %(isinstance.id, isinstance.id, filename)

locatoins=[('Farmgate','Farmgate'),('Dhanmondi','Dhanmondi'),('Wari','Wari'),]
cats=[('HomeMade','HomeMade'),('Professional', 'Professional')]
stars=[(1,1),(2,2),(3,3),(4,4),(5,5)]
class Store ( models.Model):
    name= models.CharField(max_length=100,default='store_name')
    desc = models.CharField(max_length=1000,default='default desc')
    location = models.CharField(max_length=200,choices=locatoins,default='Farmgate')
    covImg = models.ImageField(upload_to='pic_ups')
    active = models.BooleanField(default=True)
    rating = models.IntegerField(choices=stars,default=5)
    catagory = models.CharField(max_length=200,choices=cats ,default='HomeMade')
    owner= models.ForeignKey(User, default=None, on_delete=models.CASCADE)