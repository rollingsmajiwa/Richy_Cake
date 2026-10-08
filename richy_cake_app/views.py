from django.shortcuts import render, redirect, get_object_or_404
from richy_cake_app.models import Cake
from richy_cake_app.forms import CakeForm, UserRegisterForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    return render(request, "index.html")
@login_required
def cake_page(request):
    try:
        cake = Cake.objects.all()
    except Exception as e:
        print(e)
    return render(request, "cake.html", {"cake_list": cake})
@staff_member_required
def add_cake(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cake_page')
    else:
        form = CakeForm()
    return render(request, 'add_cake.html', {"form": form})
def cake_details(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    return render(request, "cake_details.html", {"cake": cake})

# register views

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
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
                auth_login(request, user)
                messages.success(request, f"Welcome Back, {username}")
                return redirect("index_page")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please correct errors in the form")

    else:
        form = CustomLoginForm()
    return render(request, "login.html", {"form": form})
        


