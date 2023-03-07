from django.contrib import admin
from property.models import Mail, Account, Game

# Register your models here.

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('login', 'password')
    search_field = ('login', 'password')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'costs', 'description', 'mail')
    search_field = ('login', 'password', 'costs', 'description', 'mail')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'costs', 'verion')
    search_field = ('name', 'costs', 'verion')

