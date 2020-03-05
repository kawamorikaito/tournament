from django.shortcuts import render
from games.models import Game

# Create your views here.

def lottery(id):
    max_participations = Game.objects.num_people.get(id=id)
