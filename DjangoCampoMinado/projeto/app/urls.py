from django.urls import path

from .views import iniciar_jogo, post_list

urlpatterns = [
    path('start/', iniciar_jogo, name='iniciar_game'),
    path('jogadas/', post_list, name='jogar_jogo'),
]