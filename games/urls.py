from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('result/', views.result, name='result'),
]

