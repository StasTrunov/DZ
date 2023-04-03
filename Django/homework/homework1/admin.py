from django.contrib import admin
from homework1.models import FPlayer,FClub,Championship

# Register your models here.

@admin.register(FPlayer)
class FPlayerAdmin(admin.ModelAdmin):
    list_fplayer = ('name', 'country', 'height','costs')
    search_field = ('name', 'country', 'height', 'costs')

@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_championship = ('name', 'country')
    search_field = ('name', 'country')

@admin.register(FClub)
class FClubAdmin(admin.ModelAdmin):
    list_fclub = ('name', 'country')
    search_field = ('name', 'country')

