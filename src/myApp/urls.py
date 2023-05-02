from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("products", views.products, name='products'),
    # path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]

