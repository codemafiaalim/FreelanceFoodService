from django.shortcuts import render
from .models import Plan
from .models import Store
from .forms import StoreForm
# Create your views here.
def plans (request):
    plans=Plan.objects.all()
    return render (request,'plans.html',{'plans': plans})
def store (request):
    stores=Store.objects.all()
    print("Going to store")
    return render (request,'stores2.html',{'stores': stores})
def createStore (request):
    form = StoreForm(request.POST or None)
    print("Before Save passed")
    if form.is_valid():
        print("Saving...")
        form.save()
        print("Save passed")
    context={
        'form': form
    }
    return render(request,"create.html",context)
def viewStores (request):
    stores=Store.objects.all()
    return render (request,'allstores.html',{'stores': stores})