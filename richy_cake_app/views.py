from django.shortcuts import render, redirect, get_object_or_404
from richy_cake_app.models import Cake
from richy_cake_app.forms import CakeForm, UserRegisterForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    try:
        cake = Cake.objects.all()
    except Exception as e:
        print(e)
    return render(request, "index.html", {"cake_list": cake})

# register views

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect("login")

    else:
        form = UserRegisterForm()
        return render(request, "register.html", {"form": form})
def custom_login(request):
    if request.user.is_authenticated:
        return redirect("index_page")

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
       
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back, {username}")
                return redirect("index_page")
            else:
                messages.error("Invalid username or password")
        else:
            messages.error("Please correct errors in the form")

    else:
        form = CustomLoginForm()
        return render(request, "login.html", {"form": form})
        


