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
    logo = models.ImageField(upload_to='media/images/education/', blank=True)

    def __str__(self):
        return self.instituition

class Extracurricular(models.Model):
    instituition = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start = models.CharField(max_length=30)
    present = models.BooleanField(default=False)
    end = models.CharField(max_length=30, blank=True, null=True)
    logo = models.ImageField(upload_to='media/images/extracurricular/', blank=True)

    def __str__(self):
        return self.instituition

class Job(models.Model):
    instituition = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start = models.CharField(max_length=30)
    present = models.BooleanField(default=False)
    end = models.CharField(max_length=30, blank=True, null=True)
    logo = models.ImageField(upload_to='media/images/jobs/', blank=True)

    def __str__(self):
        return self.instituition
