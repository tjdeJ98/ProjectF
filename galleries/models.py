from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    featured_image = models.ForeignKey(
        'Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="media/gallerie/")
    pub_date = models.DateTimeField("Date published", auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    hidden = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.image) + " - " + str(self.pub_date)
    class Meta: 
        ordering = ['pub_date']

