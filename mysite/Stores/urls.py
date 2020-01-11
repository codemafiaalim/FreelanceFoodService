from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('stall/', views.allstore),
    path('st/', views.store),
    path('create/', views.createStore)

]
