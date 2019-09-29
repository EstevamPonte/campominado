from ast import literal_eval
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime
import sys
from campoMinadoView import iniciar_novo_jogo, continuar_jogo, efetuar_nova_jogada,menu_inicial, sair, restaurar_jogo
from mensagensConstantes import CODIGO_COMANDO, CODIGO_RESPOSTA, COMANDO_EFETUAR_JOGADA, JOGADA_LINHA, JOGADA_COLUNA ,COMANDO_SHOW, IMPRIMIR, QTD

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535

def enviar(mensagem):

    dest = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)
    data = mensagem.encode(ENCODE)
    sock.sendto(data, dest)
    data, address = sock.recvfrom(MAX_BYTES)
    respota = data.decode(ENCODE)
    sock.close()

    return respota
"""Função para receber as jogadas e enviar para o servidor"""

def qtd_jogadas():
    contexto = {CODIGO_COMANDO: QTD}
    mensagem = str(contexto)
    resposta = literal_eval(enviar(mensagem))
    return (str(resposta))

def tabuleiro_show():
    contexto = {CODIGO_COMANDO: IMPRIMIR}
    mensagem = str(contexto)
    resposta = literal_eval(enviar(mensagem))
    for posicao in resposta:
        print (str(posicao))

def tratar_jogadas():
    proxima_jogada = True
    while proxima_jogada:
        contexto = {CODIGO_COMANDO: COMANDO_EFETUAR_JOGADA}
        contexto[JOGADA_LINHA] = input("[Jogada] Informe a linha: ")
        contexto[JOGADA_COLUNA] = input("[Jogada] Informe a coluna: ")
        mensagem = str(contexto)
        resposta = literal_eval(enviar(mensagem))
        qtd = qtd_jogadas()
        print('QUANTIDADE DE JOGADAS RESTANTES',qtd)
        tabuleiro_show()
        if qtd == "0":
            print("GAMEOVER !")
            proxima_jogada = False

"""Fim tratar_jogadas"""


def cliente():

    switcher = {
        1: iniciar_novo_jogo,
        2: restaurar_jogo,
        3: sair,
    }

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))

        contexto = {CODIGO_COMANDO: opcao}
        print (contexto)
        func = switcher.get(opcao)

        mensagem = func(contexto)
        print(mensagem)
        resposta = literal_eval(enviar(mensagem))
        tratar_jogadas()
        print (resposta.get("CODIGO_RESPOSTA"))



if __name__ == "__main__":
    cliente()