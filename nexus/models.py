from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    uploader = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=2000)
    summary = models.TextField(max_length=500,
                               default="",
                               blank=True)
    type = models.CharField(max_length=10)
    votes = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
