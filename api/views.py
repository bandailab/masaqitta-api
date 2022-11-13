from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Tweet, Grade
from .serializer import UserSerializer, TweetSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
