class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo #### atributo privado
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 50)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
#print(conta._saldo) ### INCORRETO SEGUNDO A CONVERSÃO
