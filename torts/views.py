from django.shortcuts import render
from .forms import CakeOrderForm
from .models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    kateg=Kategor.objects.all()
    list={
        'kateg':kateg
    }
    return render (request, 'index.html', list)
def table(request):
    kateg = Kategor.objects.all()
    list={
        'kateg':kateg
    }
    return render (request, 'table.html',list)

def torts(request, id):
    kateg_filter=Kategor.objects.filter(id=id)
    torts_filter= Cake.objects.filter(kategor=id)
    list={
        'torts_filter':torts_filter,
        'kateg_filter':kateg_filter
    }
    return render(request,'torts.html',list)
def torts_1(request, id):
    cake = Cake.objects.get(id=id)
    if request.method == 'POST':
        form = CakeOrderForm(request.POST)
        if form.is_valid():
            form.instance.cake_name = cake.name
            form.save()
    else:
        form = CakeOrderForm()
    context = {
        'cake': cake,  # Передаем объект торта в шаблон
        'form': form
    }
    return render(request, '1_tort.html', context)


