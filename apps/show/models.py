from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3:
            errors["title"] = "Title should be at least 3 characters"
        if len(postData['network']) < 1:
            errors["network"] = "Network should be at least 1 characters"
        if len(postData['release_date']) < 1:
            errors["release_date"] = "Release date should be at least 1 characters"
        if len(postData['desc']) < 3:
            errors["desc"] = "Description should be at least 3 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=55)
    release_date = models.DateTimeField()
    desc = models.TextField()
    # author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



