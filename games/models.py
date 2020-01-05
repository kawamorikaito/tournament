from django.db import models
from django.utils import timezone

class Game(models.Model):
    owner_user_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    game_name = models.CharField(max_length=50, null=True)
    num_people = models.IntegerField(default=0)
    reception_start_time = models.DateTimeField(default=timezone.now)
    reception_end_time = models.DateTimeField(default=timezone.now)
    game_start_time = models.DateTimeField(default=timezone.now)
    game_end_time = models.DateTimeField(default=timezone.now)
    outline = models.CharField(max_length=50)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name