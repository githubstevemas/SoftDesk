from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    birthdate = models.DateField()
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)
