from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    dob = models.DateField(null=True)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
#     dob = models.DateField(null=True)
#
#     class Meta:
#         abstract = True
