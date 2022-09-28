from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'

class Mac(models.Model):
    name = models.CharField(verbose_name='メニュー名', max_length=50)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    ditail = models.TextField(verbose_name='詳細', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Mac'

    def __str__(self):
        return self.name

class Mos(models.Model):
    name = models.CharField(verbose_name='メニュー名', max_length=50)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    ditail = models.TextField(verbose_name='詳細', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Mos'

    def __str__(self):
        return self.name

class BurgerKing(models.Model):
    name = models.CharField(verbose_name='メニュー名', max_length=50)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    ditail = models.TextField(verbose_name='詳細', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'BurgerKing'

    def __str__(self):
        return self.name

class Favorite(models.Model):
    mac = models.ForeignKey(Mac, verbose_name='マック', on_delete=models.PROTECT)
    mos = models.ForeignKey(Mos, verbose_name='モスバーガー', on_delete=models.PROTECT)
    burgerking = models.ForeignKey(BurgerKing, verbose_name='バーガーキング', on_delete=models.PROTECT)
   

    class Meta:
        verbose_name_plural = 'Favorite'