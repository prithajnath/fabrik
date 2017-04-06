from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):

    user = models.ForeignKey(User, null=True)
    latitude = models.FloatField(max_length=10, default=0)
    longitude = models.FloatField(max_length=10, default=0)
    home = models.BooleanField(default=True)
