import time

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404


def home_view(request):
    return render(request, 'main/main_page.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    if request.user.is_authenticated:
        return redirect("profile")
    else:
        return render(request, "main/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        return render(request, "main/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ShopCreateForm(request.POST, request.FILES)
            if form.is_valid():
                test = form.save(commit=False)
                test.seller_id = request.user
                test.save()
                return redirect('shops')
        else:
            form = ShopCreateForm()

        user = User.objects.get(id=request.user.id)
        data = {'user': user, 'form': form}
        return render(request, 'main/profile.html', data)
    else:
        return redirect("login")


def update_user(request, user_id):
    if request.user.is_authenticated and user_id == request.user.id:
        user = User.objects.get(pk=user_id)
        session_user = request.user
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = UpdateUserForm(instance=user)
        return render(request, 'main/edit_user.html', {'form': form, 'user': user, 'session_user': session_user})
    else:
        return redirect('profile')


def shops(request):
    shops = Shop.objects.all()
    context = {'shops': shops}
    return render(request, 'main/shops.html', context)


def shop_page(request, u_name):
    shop = Shop.objects.get(url_name=u_name)
    context = {'shop': shop}
    return render(request, 'main/shop_page.html', context)


def update_shop(request, u_name):
    shop = Shop.objects.get(url_name=u_name)
    if request.method == 'POST':
        form = ShopUpdateForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_page')
    else:
        form = ShopUpdateForm(request.FILES, instance=shop)
    return render(request, 'main/edit_shop.html', {'form': form, 'shop': shop})


class UpdateShop(UpdateView):
    model = Shop
    template_name = 'main/edit_shop.html'
    form_class = ShopUpdateForm
    success_url = reverse_lazy("home")
