from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Book)
class Book(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
        'import_date'
    ]



@admin.register(models.Member)
class Member(admin.ModelAdmin):
    list_display = [
        'user'
    ]


@admin.register(models.Borrowing)
class Borrowing(admin.ModelAdmin):
    list_display = [
        'book',
        'member',
        'borrowing_date',
        'borrowing_status'
    ]

