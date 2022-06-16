from django.db import models
from django.conf import settings

# Create your models here.
class Forest(models.Model):
    name = models.CharField(max_length=250)
    possession = models.CharField(max_length=250)
    facility = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    overview = models.TextField(blank=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_forests')
    stamp = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stamp_forests')

class Review(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    RATES_CHOICES = (
        (5,'5'),
        (4,'4'),
        (3,'3'),
        (2,'2'),
        (1,'1'),
    )
    rates = models.IntegerField(choices=RATES_CHOICES)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE, related_name='reviews')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

class Community(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE, related_name='communitys')       
