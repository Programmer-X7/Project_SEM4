from django.contrib import admin
from django.urls import path
from myApp import views
from .views import *

urlpatterns = [
    # User Section
    path("signup", signup, name="signup"),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logoutUser'),

    # Navbar Section
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("products", views.products, name='products'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("profile", views.profile, name='profile'),
    path("cart", views.cart, name='cart'),

    #Checkout and payment Section
    path("checkout", views.checkout, name="checkout"),

    # Product Section
    path("laptops", views.laptops, name='laptops'),
    path("mice", views.mice, name='mice'),
    path("keyboards", views.keyboards, name='keyboards'),
    path("headphones", views.headphones, name='headphones'),
    path("monitors", views.monitors, name='monitors'),
    
    # Laptop Section
    path("laptop+model+1", views.lt_model_1, name='laptop+model+1'),
    path("laptop+model+2", views.lt_model_2, name='laptop+model+2'),
    path("laptop+model+3", views.lt_model_3, name='laptop+model+3'),
    path("laptop+model+4", views.lt_model_4, name='laptop+model+4'),

    # Mice Section
    path("mice+model+1", views.mc_model_1, name='mice+model+1'),
    path("mice+model+2", views.mc_model_2, name='mice+model+2'),
    path("mice+model+3", views.mc_model_3, name='mice+model+3'),
    path("mice+model+4", views.mc_model_4, name='mice+model+4'),

    # Keyboard Section
    path("keyboards+model+1", views.kb_model_1, name='keyboards+model+1'),
    path("keyboards+model+2", views.kb_model_2, name='keyboards+model+2'),
    path("keyboards+model+3", views.kb_model_3, name='keyboards+model+3'),
    path("keyboards+model+4", views.kb_model_4, name='keyboards+model+4'),

    # Headphone Section
    path("headphones+model+1", views.hp_model_1, name='headphones+model+1'),
    path("headphones+model+2", views.hp_model_2, name='headphones+model+2'),
    path("headphones+model+3", views.hp_model_3, name='headphones+model+3'),
    path("headphones+model+4", views.hp_model_4, name='headphones+model+4'),

    # Monitor Section
    path("monitors+model+1", views.mt_model_1, name='monitors+model+1'),
    path("monitors+model+2", views.mt_model_2, name='monitors+model+2'),
    path("monitors+model+3", views.mt_model_3, name='monitors+model+3'),
    path("monitors+model+4", views.mt_model_4, name='monitors+model+4'),
    
]

