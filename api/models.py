from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(verbose_name="name", max_length=255, primary_key=True)
    color = models.CharField(verbose_name="color", max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(verbose_name="username", max_length=255, primary_key=True)
    fullname = models.CharField(verbose_name="fullname", max_length=255)
    grade = models.ForeignKey("Grade", related_name="grade", on_delete=models.CASCADE)
    image_url = models.CharField(verbose_name="image_url", max_length=255)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

class Tweet(models.Model):
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    tweet_text = models.CharField(verbose_name="tweet_text", max_length=255)
    author = models.ForeignKey("User", related_name="author", on_delete=models.CASCADE)
    favorite = models.ManyToManyField("User", related_name="favorite", blank=True)
    retweet = models.ManyToManyField("User", related_name="retweet", blank=True)
    reply = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.text

