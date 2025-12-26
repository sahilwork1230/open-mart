from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'index.html')

def cart(request):
    pass

def product_view(request):
    pass



#auth views
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():

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
