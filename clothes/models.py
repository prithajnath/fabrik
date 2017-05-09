from django.conf import settings
from django.db import models

# Create your models here.
class Clothing(models.Model):

    name = models.CharField(max_length=100)
    clothing_type = models.CharField(max_length=100, default='None')
    clothing_location = models.CharField(max_length=100, default='None')
    image = models.ImageField(upload_to='clothes/')
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    def __str__(self):
        return self.name
