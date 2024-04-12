from django.contrib import admin
from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'category', 'pub_date', 'hidden']
    list_editable = ['category', 'hidden']
    list_per_page = 25

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_image']
    # list_editable = ['title']
    # list_per_page = 25
