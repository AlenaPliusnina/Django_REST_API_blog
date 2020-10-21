from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    slug = models.SlugField
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name='posts')
