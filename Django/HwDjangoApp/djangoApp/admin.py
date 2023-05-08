from django.contrib import admin
from .models import Article



@admin.register(Article)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'body', 'created_at', 'modified_at')