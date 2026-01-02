from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'index.html')

def product_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    products = category.products.all()
    return render(request, f'products/{category_slug}.html', {"products": products})

def product_detail(request, product_title, product_id):
    product = get_object_or_404(Product, id = product_id)

    return render(request, 'products/product-details.html', {'product':product})





#auth views
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise ValidationError("A user with this email already exists!")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            return redirect('/login/')
    form = SignupForm()
    return render(request, 'auth/signup.html', {'form':form})
            


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=identifier, password=password)
            if user:
                login(request, user)
                return redirect("home")

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def reset_password(request):
    pass
