from django.shortcuts import render


def index(request):
    return render(request, "pages/home.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def products(request):
    return render(request, "pages/products.html", {})

def services(request):
    return render(request, "pages/services.html", {})

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



def lt_model_1(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model1.html", {})

def lt_model_2(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model2.html", {})

def lt_model_3(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model3.html", {})

def lt_model_4(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model4.html", {})