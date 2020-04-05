from django.db import models
from django.utils import timezone


class Post(models.Model):
    content = models.TextField()
    upload = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)