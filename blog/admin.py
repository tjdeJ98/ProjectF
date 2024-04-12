from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    filter_horizontal = ('images',)  # Provides a nice interface for multiple images

admin.site.register(BlogPost, BlogPostAdmin)