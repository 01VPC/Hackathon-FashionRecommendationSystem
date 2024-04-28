from django.db import models

# Create your models here.
from django.db import models

class Outfit(models.Model):
    gender = models.CharField(max_length=50)
    mastercategory = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    articletype = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)

class FashionItem(models.Model):
    productDisplayName = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    subCategory = models.CharField(max_length=255)
    baseColour = models.CharField(max_length=255)
    articleType = models.CharField(max_length=255)
    masterCategory = models.CharField(max_length=255)
    usage = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.productDisplayName