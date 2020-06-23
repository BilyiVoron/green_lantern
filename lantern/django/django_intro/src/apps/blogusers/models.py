from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    dob = models.DateField(null=True)
