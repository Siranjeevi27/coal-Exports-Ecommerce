from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('products', views.products,name="products"),
    path('login', views.login,name="login"),
    path('sighup', views.sighup,name="sighup"),
    path('logout',views.logout,name='logout'),
   
]