from django.db import models

# Create your models here.
class LevelClear(models.Model):
    name = models.CharField(max_length=20)
    cleared = models.BooleanField(default=False)