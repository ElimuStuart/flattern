from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    overview = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=120, unique_for_date=timestamp)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title

    


