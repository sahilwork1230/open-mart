from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm
from .models import Category, Product
from .forms import AddressForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories})

def product_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all()
    
    template_name = f'products/{category_slug}.html'
    try:
        get_template(template_name)
    except TemplateDoesNotExist:
        template_name = 'products/category.html'
        
    return render(request, template_name, {"products": products, "category": category})

def product_detail(request, product_title, product_id):
    product = get_object_or_404(Product, id = product_id)

    return render(request, 'products/product-details.html', {'product':product})

@login_required(login_url='login')
def add_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            print("ADDRESS SAVED")
        else:
            print("FORM ERRORS:", form.errors)
    return redirect("checkout")


#auth views
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form':form})
            


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=identifier, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def reset_password(request):
    pass

from orders.models import Order

def test(request):
    return render(request, 'test.html')

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')
    addresses = user.addresses.all()
    return render(request, 'auth/profile.html', {
        'user': user,
        'orders': orders,
        'addresses': addresses
    })

@login_required(login_url='login')
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'auth/order_detail.html', {'order': order})


def product_details(request, slug):
    pass