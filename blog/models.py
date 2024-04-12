from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from galleries.models import Image

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    images = models.ManyToManyField(Image, blank=True)  # Allow multiple images per post
    created_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title