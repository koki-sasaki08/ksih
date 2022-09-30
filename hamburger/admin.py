from django.contrib import admin
from .models import CustomUser

from .models import Mac, Mos, BurgerKing, FavoriteMac

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Mac)
admin.site.register(Mos)
admin.site.register(BurgerKing)
admin.site.register(FavoriteMac)