from django.db import models
from django.contrib.auth.models import AbstractUser

# default -> django -> auth.user | if -> settings.py -> AUTH_USER_MODEL = 'STH' -> django checks settings.py


class CustomUser(AbstractUser):  # name, lastname, username, email, password, ...+ age
    age = models.PositiveIntegerField()
