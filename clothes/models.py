from django.db import models

# Create your models here.
class Clothing(models.Model):

    name = models.CharField(max_length=100)
    clothing_type = models.CharField(max_length=100)
    img_location = models.URLField(max_length=200)

    def __str__(self):
        return self.name
