from django.db import models
from django.conf import settings


# Create your models here.
class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('teacher.Course', on_delete=models.CASCADE)

