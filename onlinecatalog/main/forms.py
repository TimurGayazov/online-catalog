from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, PasswordInput, FileInput, FloatField, \
    CharField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from django.utils.timezone import datetime
from image_cropping import ImageCropWidget



class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите логин'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите почту'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Повторите пароль'}))
    user_role = forms.ModelChoiceField(queryset=Role.objects.all(),
                                       widget=forms.Select(attrs={"class": "form-select", 'placeholder': ''}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "user_role"]


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите логин'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите почту'}))
    user_role = forms.ModelChoiceField(queryset=Role.objects.all(),
                                       widget=forms.Select(attrs={"class": "form-select", 'placeholder': ''}))
    last_update = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите дату'}), initial=datetime.now())

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "user_role", "last_update"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class ShopCreateForm(ModelForm):
    url_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите url магазина'}))
    shop_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите название магазина'}))
    subject_matter = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(
        attrs={"class": "form-select", 'placeholder': 'Выберети категорию'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Введите описание магазина', 'rows': 3}))
    seller_id = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={"class": "form-select", 'placeholder': 'Выберети категорию'}), initial='e')
    # cover_image = forms.ImageField(widget=ImageCropWidget(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Shop
        fields = ['url_name', 'shop_name', 'subject_matter', 'description', 'seller_id']


class ShopUpdateForm(ModelForm):
    url_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите url магазина'}))
    shop_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите название магазина'}))
    subject_matter = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(
        attrs={"class": "form-select", 'placeholder': 'Выберети категорию'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Введите описание магазина', 'rows': 3}))
    seller_id = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(
        attrs={"class": "form-select", 'placeholder': 'Выберети категорию'}), initial='e')
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    telegram_link = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите ссылку на телеграм'}))
    instagram_link = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите ссылку на инстаграм'}))
    vk_link = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите ссылку на вк'}))
    other_link = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите дополнительную'}))


    class Meta:
        model = Shop
        fields = ['url_name', 'shop_name', 'subject_matter', 'description', 'seller_id', 'cover_image', 'avatar', 'telegram_link',
                  'instagram_link', 'vk_link', 'other_link']
