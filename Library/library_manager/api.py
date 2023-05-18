
import time
import json
import pytz
import pandas as pds


from django.shortcuts import render, redirect
from PIL import Image
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from . import models
from . import serializers

# Check Authentication

@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def is_authenticated(request):
    is_authenticate = False
    is_superuser = False
    try:
        is_authenticate = '_auth_user_id' in request.session
        if is_authenticate:
            is_superuser = User.objects.get(
                id=request.session['_auth_user_id']).is_superuser

    except:
        is_authenticate = False

    print(f"auth : {is_authenticate} superuser : {is_superuser}")

    return Response({"is_authenticated": is_authenticate, "is_superuser": is_superuser})


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def getAllBook(request):
    all_book = models.Book.objects.all()
    data = serializers.AllBookSerializer(all_book, many=True).data
    
    return Response(data)
