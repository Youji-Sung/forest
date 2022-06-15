from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile/', default='profile/None.png')
    nickname = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()