class Passaro:
    def voar(self):
        print("Passaros Voão...")


class Pardal(Passaro):
    def voar(self):  ### modificando o metodo Voar##
        super().voar()
       


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(quem_voa): ### POLIMORFISMO
    quem_voa.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
