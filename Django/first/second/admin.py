from django.contrib import admin
from second.models import Author, Post, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display__ = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display_ = ('author', 'text', 'like', 'dislike')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
