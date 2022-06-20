from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField()
    RDate= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)