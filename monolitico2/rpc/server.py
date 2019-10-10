import rpyc
from rpyc.utils.server import ThreadedServer
from negocioCampoMinado import CampoMinado

class MyService(rpyc.Service):

    def exposed_criar_novo_jogo(self, num_bomb):
        self.campo_minado = CampoMinado(num_bomb)

    def exposed_get_lista_bomb(self):
        return self.campo_minado.get_lista_bomb()

def server():    
    t = ThreadedServer(MyService, port = 18861)
    t.start()

server()