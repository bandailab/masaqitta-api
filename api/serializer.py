from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User, Tweet, Grade

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'fullname', 'grade', 'image_url', 'created_at', 'following')

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('created_at', 'tweet_text', 'author', 'favorite', 'retweet', 'reply')
