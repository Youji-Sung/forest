from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)