from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm
from .models import Category, Product
from .forms import AddressForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
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

            from django.contrib import messages
            messages.success(request, f"Welcome {user.first_name}! Your account has been created successfully.")

            # Welcome email sending logic
            subject = "Signup Success"
            mail_message = f"Greetings {user.first_name}! You have successfully registered with Nexora with your email {user.email}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            try:
                send_mail(subject, mail_message, email_from, recipient_list)
            except Exception as e:
                print(f"Failed to send mail: {e}")


            return redirect('/login/')
        else:
            # Send form errors as toast messages
            from django.contrib import messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.replace('_', ' ').title()}: {error}")
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form':form})
            


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get("identifier")
            password = form.cleaned_data.get("password")
            print(identifier)

            user = authenticate(request, username=identifier, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get("next")
                
                from django.contrib import messages
                messages.success(request, f"Welcome back, {user.username}!")

                return redirect(next_url if next_url else "home")
            
            # form.add_error(None, "Invalid credentials")
            from django.contrib import messages
            messages.error(request, "Invalid credentials. Please check your username/email and password.")

    else:
        form = LoginForm()

    return render(request, 'auth/login.html',{"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

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