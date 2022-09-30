from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'

class Mac(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='id', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='メニュー名', max_length=50)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    ditail = models.TextField(verbose_name='詳細', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Mac'

    def __str__(self):
        return self.name

class Mos(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='id', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='メニュー名', max_length=50)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    ditail = models.TextField(verbose_name='詳細', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Mos'

    def __str__(self):
        return self.name

class BurgerKing(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='id', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='メニュー名', max_length=50)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    ditail = models.TextField(verbose_name='詳細', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'BurgerKing'

    def __str__(self):
        return self.name


class FavoriteMac(models.Model):
    mac = models.ForeignKey(Mac, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'FavoriteMac'