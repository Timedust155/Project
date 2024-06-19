from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from torts.models import *
from .forms import *
from django.views.generic import UpdateView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    kateg = Kategor.objects.all()
    list = {
        'kateg': kateg
    }
    return render(request, 'register.html', {'form': form,'list':list})


@login_required
class profile_update(UpdateView):
    model = Kategor

    template_name = 'users/update.html'
    fields = ['name']

def profile_update(request, id):

    cake = Cake.objects.get(id=id)
    if request.method == 'POST':
        form = CakeForm(request.POST, instance=cake)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CakeForm(instance=cake)
    return render(request, 'profile_update.html', {'form': form})


def delete_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    cake.delete()
    kateg = Cake.objects.all()
    list = {
        'kateg': kateg
    }
    return render(request, 'profile.html', list)
def zakaz(request):
    zakaz= CakeOrder.objects.all()
    list = {
        'zakaz': zakaz
    }
    return render(request, 'profile_delite.html',list)
def delete_zakaz(request, cake_id):
    cake = CakeOrder.objects.get(cake_id1=cake_id)
    cake.delete()
    zakaz = CakeOrder.objects.all()
    list = {
        'zakaz': zakaz
    }
    return render(request, 'profile_delite.html', list)

def zakaz_update(request, id):

    cake = CakeOrder.objects.get(cake_id1=id)
    if request.method == 'POST':
        form = CakeOrderForm(request.POST, instance=cake)
        if form.is_valid():
            form.save()
            return redirect('zakaz')
    else:
        form = CakeOrderForm(instance=cake)
    return render(request, 'profile_update.html', {'form': form})


def profile(request):
    kateg = Cake.objects.all()


    list = {
        'kateg': kateg
    }
    return render(request, 'profile.html',list)