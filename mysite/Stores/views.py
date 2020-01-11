from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from flask import request
from . import forms
from .models import Store
from .forms import StoreForm
from django.core.files.storage import FileSystemStorage


def createStore(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            ins = form.save()
            ins.owner = request.user
            ins.save()
            return redirect('/')
    else:
        form = forms.StoreForm()
    return render(request, 'create.html', {'form': form})


# Create your views here.
def allstore(request):
    stores = Store.objects.all()
    print("Going to store")
    return render(request, 'store4all.html', {'stores': stores})


def store(request):
    stores = Store.objects.filter(owner=request.user)
    print("Going to store")
    return render(request, 'stores4.html', {'stores': stores})


def success(request):
    return HttpResponse('successfully uploaded')
