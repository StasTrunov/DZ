from django.contrib import admin
from school.models import Student,Class,School

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_fplayer = ('name', 'email', 'age', 'second_name')
    search_field = ('name', 'email', 'age', 'second_name')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_championship = ('name', 'age')
    search_field = ('name', 'age')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_fclub = ('name', 'country')
    search_field = ('name', 'country')
