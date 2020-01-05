from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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
        name=request.POST['name'],
        num_people=request.POST['num_people'],
        outline=request.POST['outline'],
        reception_start_time=request.POST['reception_start_time'],
        reception_end_time=request.POST['reception_end_time'],
        game_start_time=request.POST['game_start_time'],
        game_end_time=request.POST['game_end_time'],
        game_name=request.POST['game_name'],
        owner_user_code="hogehoge"

    )

    game.save()

    game_list = Game.objects.order_by('id')[:5]
    template = loader.get_template('games/index.html')
    context = {
        'game_list': game_list,
    }
    return HttpResponse(template.render(context, request))
