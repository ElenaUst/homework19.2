from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=250, verbose_name='токен пользователя', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

