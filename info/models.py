from django.db import models

# Create your models here.
class Education(models.Model):
    instituition = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    start = models.CharField(max_length=30)
    present = models.BooleanField(default=False)
    end = models.CharField(max_length=30, blank=True, null=True)
    result = models.CharField(max_length=30, blank=True, null=True)
    logo = models.ImageField(upload_to='media/images/', blank=True)
