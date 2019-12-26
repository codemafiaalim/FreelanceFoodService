from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
def home (request):
    return render (request,'index.html')
def makemoney (request):
    return render(request,'makemoneypage.html')


