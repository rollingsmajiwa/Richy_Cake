from django.shortcuts import render, redirect, get_object_or_404
from richy_cake_app.models import Cake, Cart
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

@login_required
def add_cake(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.error(request, "Access Restricted! You must be an Admin")
        return redirect('cake_page')


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

# cart item
@login_required
def add_to_cart(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, cake=cake)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Updated {cake.name} quantity in your cart.")
    else:
        messages.success(request, f"Added {cake.name} to your cart.")
        
    return redirect('cart_detail')

# 2. View
@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.subtotal() for item in cart_items)
    
    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


#  Delete
@login_required
def delete_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    messages.info(request, "Item removed from cart.")
    return redirect('cart_detail')


