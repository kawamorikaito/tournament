from django.db import models
from django.utils import timezone

class Game(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    num_people = models.IntegerField(default=0)
    start_time = models.DateTimeField(default=timezone.now)
    outline = models.CharField(max_length=50)

    def __str__(self):
        return self.name