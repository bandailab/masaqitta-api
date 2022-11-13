from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User, Tweet, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('name', 'color')

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'grade', 'image_url')

class UserSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    following = FollowingSerializer(many=True)
    
    class Meta:
        model = User
        fields = ('username', 'fullname', 'created_at','grade', 'image_url', 'following')

class ReplySerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Tweet
        fields = ('tweet_text', 'created_at', 'author', 'favorite', 'retweet')

class TweetSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    favorite = UserSerializer(many=True)
    retweet = UserSerializer(many=True)
    reply = ReplySerializer(many=True) # //error has occured

    class Meta:
        model = Tweet
        fields = ('tweet_text', 'created_at', 'author', 'favorite', 'retweet', 'reply')
