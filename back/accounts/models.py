from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile/', default='profile/None.png')
    nickname = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True)

# class UserManager(BaseUserManager):
#     def create_superuser(self, email, password):
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
