from django import forms
from torts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CakeOrderForm(forms.ModelForm):
    class Meta:
        model = CakeOrder
        fields = ['phone_number', 'order_description']
        labels = {
            'phone_number': 'Телефон',
            'order_description': 'Пожелания',
        }
class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'description',  'price']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']