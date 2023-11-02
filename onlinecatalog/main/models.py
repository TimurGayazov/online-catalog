from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils.timezone import datetime
from phonenumber_field.modelfields import PhoneNumberField
from image_cropping.fields import ImageCropField



class Role(models.Model):
    role_name = models.CharField('Название роли', max_length=50)

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class User(AbstractUser):
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    last_update = models.DateField(null=True, default=datetime.now())


class Subject(models.Model):
    subject_name = models.CharField('Название тематики', max_length=100)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Shop(models.Model):
    url_name = models.CharField('url', primary_key=True, max_length=50)
    shop_name = models.CharField('Название магазина', max_length=100)
    subject_matter = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField('Описание магазина', max_length=5000, null=True)
    cover_image = models.ImageField(upload_to='shop_covers/', null=True, blank=True)
    avatar = models.ImageField(upload_to='shop_avatars/', null=True, blank=True)
    address = models.CharField('Адрес магазина', max_length=1000, null=True, blank=True)
    phone = PhoneNumberField('Телефон', null=True, blank=True)
    telegram_link = models.CharField('Ссылка на телеграм аккаунт магазина', max_length=200, null=True, blank=True)
    instagram_link = models.CharField('Ссылка на инстраграм аккаунт магазина', max_length=200, null=True, blank=True)
    vk_link = models.CharField('Ссылка на вк аккаунт магазина', max_length=200, null=True, blank=True)
    other_link = models.CharField('Другая ссылка', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.shop_name

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
