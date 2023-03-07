from django.contrib import admin
from second.models import Author, Post, Category


@admin.register(Author)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Post)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'like', 'dislike')


@admin.register(Category)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name',)
