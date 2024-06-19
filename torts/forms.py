
from .models import CakeOrder
from django import forms



class CakeOrderForm(forms.ModelForm):
    class Meta:
        model = CakeOrder
        fields = ['phone_number', 'order_description']
        labels = {
            'phone_number': 'Телефон',
            'order_description': 'Пожелания',
        }