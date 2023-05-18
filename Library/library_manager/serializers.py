from django.contrib.auth.models import User, Group
from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AllBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'