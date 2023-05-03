from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("products", views.products, name='products'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("laptops", views.laptops, name='laptops'),
    path("mice", views.mice, name='mice'),
    path("keyboards", views.keyboards, name='keyboards'),
    path("headphones", views.headphones, name='headphones'),
    path("monitors", views.monitors, name='monitors'),
    
    path("laptop+model+1", views.lt_model_1, name='laptop+model+1'),
    path("laptop+model+2", views.lt_model_2, name='laptop+model+2'),
    path("laptop+model+3", views.lt_model_3, name='laptop+model+3'),
    path("laptop+model+4", views.lt_model_4, name='laptop+model+4'),
]

