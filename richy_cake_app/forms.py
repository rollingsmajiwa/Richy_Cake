from django import forms
from richy_cake_app.models import Cake
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ["name", "description", "price", "image"]

# overriding usercreation form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

# overriding username and password
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())