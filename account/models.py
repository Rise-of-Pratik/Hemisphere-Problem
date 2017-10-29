import datetime

from mongoengine import *
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from mongoengine.django.auth import User


# Create your models here.

class User(User):
    """
    creates account models
    """
    email = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, default="")
    middle_name = models.CharField(max_length=254, blank=True, default="")
    last_name = models.CharField(max_length=254, default="")
    phone = models.CharField(max_length=10, default="", unique=True)
    picture = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'id'

    # objects = account_manager.CustomUserManager()
    #
    def __str__(self):
        return self.email
