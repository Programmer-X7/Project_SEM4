from django.shortcuts import render


def index(request):
    return render(request, "pages/home.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def products(request):
    return render(request, "pages/products.html", {})

# def index(request):
#     return render(request, "pages/service.html", {})

def contact(request):
    return render(request, "pages/contact.html", {})