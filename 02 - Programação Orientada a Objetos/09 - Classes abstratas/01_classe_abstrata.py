###>>>> MODULO DE CLASS ABSTRACT <<<####
from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    pilhas = 2
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def tipo_pilha(self):
        pass


class ControleTV(ControleRemoto):
    
    def ligar(self):
        
        print("Ligando a TV...")
        print("Ligada!")
        

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def tipo_pilha(self):
        return "AAA"


class ControleArCondicionado(ControleRemoto):
    
     
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")
        

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def tipo_pilha(self):
        return "AAA"

def mostrar_dados(*objs):
    for obj in objs:
        print(obj)

controle = ControleTV()
controle.ligar()
controle.desligar() 
mostrar_dados(controle.tipo_pilha   )


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()

print(controle)
