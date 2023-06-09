from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm


# User Section

# superUser
# UN: BCET
# PW: BCET@123

# UN: suman
# PW: sumanmondal@S7

# UN: user2
# PW: sumanmondal@S72



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "pages/profile.html")
        else:
            return render(request, "login.html")
        
    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/")


# Navbar section 
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

def profile(request):
    if request.user.is_anonymous:
        return redirect(("/login"))
    return render(request, "pages/profile.html", {})

def cart(request):
    return render(request, "pages/cart.html", {})


# Checkout and Payment Section
def checkout(request):
    if request.user.is_anonymous:
        return redirect(("/login"))
    return render(request, "pages/checkout.html", {})


# Product Section 
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


# Laptop Section 
def lt_model_1(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model1.html", {})

def lt_model_2(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model2.html", {})

def lt_model_3(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model3.html", {})

def lt_model_4(request):
    return render(request, "pages/product_pages/laptop_pages/lt-model4.html", {})


# Mice Section 
def mc_model_1(request):
    return render(request, "pages/product_pages/Mice_pages/mc-model1.html", {})

def mc_model_2(request):
    return render(request, "pages/product_pages/Mice_pages/mc-model2.html", {})

def mc_model_3(request):
    return render(request, "pages/product_pages/Mice_pages/mc-model3.html", {})

def mc_model_4(request):
    return render(request, "pages/product_pages/Mice_pages/mc-model4.html", {})

# Keyboard Section
def kb_model_1(request):
    return render(request, "pages/product_pages/keyboard_pages/kb-model1.html", {})

def kb_model_2(request):
    return render(request, "pages/product_pages/keyboard_pages/kb-model2.html", {})

def kb_model_3(request):
    return render(request, "pages/product_pages/keyboard_pages/kb-model3.html", {})

def kb_model_4(request):
    return render(request, "pages/product_pages/keyboard_pages/kb-model4.html", {})


# headphones Section
def hp_model_1(request):
    return render(request, "pages/product_pages/headphone_pages/hp-model1.html", {})

def hp_model_2(request):
    return render(request, "pages/product_pages/headphone_pages/hp-model2.html", {})

def hp_model_3(request):
    return render(request, "pages/product_pages/headphone_pages/hp-model3.html", {})

def hp_model_4(request):
    return render(request, "pages/product_pages/headphone_pages/hp-model4.html", {})


# monitors Section 
def mt_model_1(request):
    return render(request, "pages/product_pages/monitor_pages/mt-model1.html", {})

def mt_model_2(request):
    return render(request, "pages/product_pages/monitor_pages/mt-model2.html", {})

def mt_model_3(request):
    return render(request, "pages/product_pages/monitor_pages/mt-model3.html", {})

def mt_model_4(request):
    return render(request, "pages/product_pages/monitor_pages/mt-model4.html", {})