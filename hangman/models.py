from django.db import models

# Create your models here.
class Phrase(models.Model):
    phrase = models.TextField()
    success = models.BooleanField(default=False)
    wrong_tries = models.PositiveSmallIntegerField(default=0)