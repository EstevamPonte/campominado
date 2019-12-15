from random import randint

from django.db import models
from django.utils import timezone
# Create your models here.

class Jogada(models.Model):
    linha = models.CharField(max_length=2)
    coluna = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)

class Game(models.Model):
    borda = models.IntegerField(default=8)
    tamanho = models.IntegerField(default=64)

    @staticmethod
    def novo_jogo():
        game = Game()
        game.save()
        Game.criar_bombas(game=game)

    @staticmethod
    def criar_bombas(area_bomba=20, game=None):

        porc_bomba = area_bomba / 100
        qtd_bomba = int(game.tamanho * porc_bomba)

        while qtd_bomba > 0:
            Game.verificar_posicao_bomba(posicao=randint(1, game.tamanho), list_bombas=list_bombas)
            qtd_bomba -= 1

    @staticmethod
    def verificar_posicao_bomba(self, posicao, ):
        if posicao in list_bombas:
            if posicao == self.tamanho:
                posicao = 0
            posicao += 1

            self.verificar_posicao_bomba(posicao, list_bombas)
            return
        list_bombas.append(posicao)

class Bomba(models.Model):
    posicaoBomba = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
