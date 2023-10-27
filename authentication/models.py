from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USER_ROLES = (
        (True, 'admin'),
        (False, 'user'),
    )
    points = models.IntegerField(null=False, blank=False, default=0)
    is_admin = models.BooleanField(choices=USER_ROLES, default=False)
