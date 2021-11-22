from django.db import models

# Create your models here.
class Club (models.Model):
    club_name = models.CharField (max_length=50)
    coutry = models.CharField (max_length=3)
    rating = models.IntegerField ()