from django.urls import path

from . import views

app_name = 'participations'
urlpatterns = [

    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('result/', views.result, name='result'),
]

