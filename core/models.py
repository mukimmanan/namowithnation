import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
from nationwithnamo import settings


class UserProfileManager(BaseUserManager):
    """ Manager For User Profiles """
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email Not Specified")
        else:
            email = self.normalize_email(email)
            user = self.model(email=email, name=name)
            user.set_password(raw_password=password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, name, password):
        """ Create and save a new super user with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve Full Name Of User """
        return self.name

    def get_short_name(self):
        """ Retrieve Short Name Of User """
        return self.name

    def __str__(self):
        """ Retrieve String Representation of our user """
        return self.email


class UserTweets(models.Model):
    """" Creating Tweets For The Users """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tweets")
    tweet_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet_text
