from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=64)
    cats_icon = models.ImageField(upload_to='media/categoryIcon')



class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_year = models.CharField(max_length=255)
    category = models.CharField(max_length=128)
    quantity = models.IntegerField()
    import_date = models.DateField(auto_now_add=True)
    book_img = models.ImageField(upload_to='media/books')

    def __str__(self):
        return self.title


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    province = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    subDistrict = models.CharField(max_length=128)
    detail = models.TextField(max_length=512)


BORROWING_STATUS = [
    ("BR", "Borrowing"),
    ("RE", "Returned"),
]

class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    borrowing_status = models.CharField(max_length=3, choices=BORROWING_STATUS)
