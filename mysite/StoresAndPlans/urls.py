from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.plans),
    path('st/', views.store),
    path('create/', views.createStore),
    path('allstores/', views.viewStores)  # might delete later

]