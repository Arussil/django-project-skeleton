from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Extend the user for further use
    TODO: Encryption by user
    """
    pass
