from django.template import loader

from django.http import Http404

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Game

# Create your views here.
def index(request):
    game_list = Game.objects.order_by('id')[:5]
    template = loader.get_template('games/index.html')
    context = {
        'game_list': game_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('games/create.html')

    return render(request, 'games/create.html')

def detail(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    return render(request, 'games/detail.html', {'game': game})

def result(request):
    game = Game(
        code=request.POST['code'],
        name=request.POST['name'],
        num_people=request.POST['num_people'],
        outline=request.POST['outline']
    )

    game.save()

    game_list = Game.objects.order_by('id')[:5]
    template = loader.get_template('games/index.html')
    context = {
        'game_list': game_list,
    }
    return HttpResponse(template.render(context, request))