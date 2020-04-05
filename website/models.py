from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    upload = models.ImageField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)