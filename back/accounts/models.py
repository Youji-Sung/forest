from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True)
    stamp = models.CharField(null=True)