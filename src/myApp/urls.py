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
]

