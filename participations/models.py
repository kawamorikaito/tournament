from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from games.models import Game


class Participations(models.Model):
    Game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    redist_time = models.DateTimeField(default=timezone.now)
    is_check_in = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name