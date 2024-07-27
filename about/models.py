from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='')
    message=models.TextField(max_length=500)

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
