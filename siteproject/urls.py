
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sites.urls')),
    path("register/",views.registerPage,name='register'),
    path("login/",views.loginPage,name='login'),                
    path("logout/",views.logoutPage,name='logout'),
]
