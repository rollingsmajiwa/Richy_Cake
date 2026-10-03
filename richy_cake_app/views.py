from django.shortcuts import render, redirect, get_object_or_404
from richy_cake_app.models import Cake
from richy_cake_app.forms import CakeForm

# Create your views here.
def index(request):
    try:
        cake = Cake.objects.all()
    except Exception as e:
        print(e)
    return render(request, "index.html", {"cake_list": cake})

