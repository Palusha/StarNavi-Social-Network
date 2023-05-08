from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_request = models.DateTimeField(verbose_name='Last request', blank=True, null=True)

    USERNAME_FIELD = 'username'
