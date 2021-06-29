from django.db import models

class Show(models.Model):
    Title = models.CharField(max_length=255)
    Network = models.CharField(max_length=255)
    Release_Date = models.DateField()
    Description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
