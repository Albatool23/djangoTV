from django.db import models


class Manager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["tital"] = "title should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "desc name should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network name should be at least 3 characters"
        return errors



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField()
    RDate= models.CharField(max_length=255)
    # desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()