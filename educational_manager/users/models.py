from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=(
            ("Administrator", "Administrator"),
            ("Teacher", "Teacher"),
            ("Student", "Student"),
        )
    )
