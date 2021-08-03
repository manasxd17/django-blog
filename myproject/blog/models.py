from django.db import models

class blog_post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

