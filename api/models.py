from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(verbose_name="name", max_length=255, primary_key=True)
    color = models.CharField(verbose_name="color", max_length=255)

    def __str__(self):
        return self.name

class Tweet(models.Model):
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    tweet_text = models.CharField(verbose_name="tweet_text", max_length=255)
    author = models.ForeignKey("User", related_name="author", on_delete=models.CASCADE)
    favorite = models.ManyToManyField("User", related_name="favorite", blank=True)
    retweet = models.ManyToManyField("User", related_name="retweet", blank=True)
    reply = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.text

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('You have to set is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('You have to set is_superuser=True.')
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_("username"), max_length=50, validators=[username_validator], unique=True, primary_key=True)
    fullname = models.CharField(verbose_name="fullname", max_length=255, blank=True)
    grade = models.ForeignKey("Grade", related_name="grade", on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.CharField(verbose_name="image_url", max_length=255, blank=True)
    following = models.ManyToManyField("self", blank=True)
    # email = models.EmailField(_("email_address"), unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "username"
    USER_ID_FIELD = "username"
    EMAIL_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()

    def __str__(self):
        return self.username
