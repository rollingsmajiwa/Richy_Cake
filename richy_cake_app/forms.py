from django import forms
from richy_cake_app.models import Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ["name", "description", "price", "image"]