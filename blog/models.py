from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField(default=timezone.now())
    content = RichTextField()
    slug = models.SlugField(primary_key=True, unique=True, default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:155]
