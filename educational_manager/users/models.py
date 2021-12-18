from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=False)
    role = models.Charfield(
        max_length=20,
        choices=(
            ("Administrator", "Administrator"),
            ("Teacher", "Teacher"),
            ("Student", "Student"),
        )
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []