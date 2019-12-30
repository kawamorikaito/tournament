from django.db import models
from django.utils import timezone

from games.models import Game

class Participations(models.Model):
    Game = models.ForeignKey(Game)
    user_code = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    redist_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name