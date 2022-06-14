from django.db import models
from django.conf import settings
from forests.models import Forest

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    using_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE)
    article_image = models.ImageField(upload_to='article/', null=True)



class Comment(models.Model):
    content = models.CharField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)