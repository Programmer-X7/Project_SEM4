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



def laptops(request):
    return render(request, "pages/product_pages/laptops.html", {})

def mice(request):
    return render(request, "pages/product_pages/mice.html", {})

def keyboards(request):
    return render(request, "pages/product_pages/keyboards.html", {})

def headphones(request):
    return render(request, "pages/product_pages/headphones.html", {})

def monitors(request):
    return render(request, "pages/product_pages/monitors.html", {})