
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = 'Site Project '                   
admin.site.index_title = 'Site Project administration'         
admin.site.site_title = 'Site Project administration' 

urlpatterns = [
    path('', views.home, name="home"),
]




