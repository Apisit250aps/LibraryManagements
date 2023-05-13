# Generated by Django 4.1.7 on 2023-05-13 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('publication_year', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('import_date', models.DateField(auto_now_add=True)),
                ('book_img', models.ImageField(upload_to='media/books')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('cats_icon', models.ImageField(upload_to='media/categoryIcon')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=128)),
                ('district', models.CharField(max_length=128)),
                ('subDistrict', models.CharField(max_length=128)),
                ('detail', models.TextField(max_length=512)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('borrowing_status', models.CharField(choices=[('BR', 'Borrowing'), ('RE', 'Returned')], max_length=3)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_manager.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_manager.member')),
            ],
        ),
    ]