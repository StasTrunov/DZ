from django.contrib import admin
from .models import Product
from .models import Prog_languages
from .models import Tennis_players


@admin.register(Product)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'like', 'dislike')

@admin.register(Prog_languages)
class SettingAdmin2(admin.ModelAdmin):
    list2 = ('name',  'date_of_creation', 'like', 'dislike')


@admin.register(Tennis_players)
class SettingAdmin3(admin.ModelAdmin):
    list3 = ('name', 'age', 'height', 'ranked_in_ATP', 'majors', 'like', 'dislike')




