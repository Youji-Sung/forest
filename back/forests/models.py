from django.db import models
from django.conf import settings

# Create your models here.
class Forest(models.Model):
    name = models.CharField()
    possession = models.CharField()
    facility = models.CharField(null=True)
    address = models.CharField(null=True)
    phone = models.CharField(null=True)
    image = models.ImageField(null=True)
    overview = models.TextField(null=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_forests')

class Review(models.Model):
    title = models.CharField()
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
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')



