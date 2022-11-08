from django.db import models

class New(models.Model):
    title = models.CharField(max_length=255)