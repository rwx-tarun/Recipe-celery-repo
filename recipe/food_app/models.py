from sre_constants import MAX_UNTIL
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name
