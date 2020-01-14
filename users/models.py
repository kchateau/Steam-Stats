from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    steam_id = models.CharField(max_length=32, default=0)

