from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile/')
    nickname = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True)
