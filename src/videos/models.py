from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    videos_id = models.CharField(max_length=50)