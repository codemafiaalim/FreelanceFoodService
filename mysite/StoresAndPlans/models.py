from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Plan(models.Model):
    title= models.CharField(max_length=100)
    catagory = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=100, default=39.99)
    desImg = models.ImageField()
    def __unicode__(self):
         return self.title
class Store ( models.Model):
    title= models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    adrs = models.CharField(max_length=200)
    covImg = models.ImageField()
    active = models.BooleanField(default=True)
    owner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __unicode__(self):
         return self.title