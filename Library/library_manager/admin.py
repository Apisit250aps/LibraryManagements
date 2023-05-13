from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Book)
class Book(admin.ModelAdmin):
    list_display = [
        'title',
        'author'
    ]



@admin.register(models.Member)
class Member(admin.ModelAdmin):
    list_display = [
        'user'
    ]

