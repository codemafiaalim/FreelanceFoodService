from django.contrib import admin
from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #none messes with urls. Write your urls under your name.
    #Durjoy

    path('admin/', admin.site.urls),
    path('mm/st/', include('Stores.urls')),
    path('mm/ac/', include('accounts.urls')),
    path('contact/ac/', include('accounts.urls')),
    path('mm/', views.makemoney),
    #path('contact/', views.contact),
    path('', views.home)
    #Alim

    #Rakib

    #Fahim
]