from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class PreguntadosUser(AbstractUser):
    """ Custom User Model """
    about_me = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(blank=True)