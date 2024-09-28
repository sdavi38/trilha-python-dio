class Foo:
    def __init__(self, x = None):
        self._x = x

    @property  ### DEPURADOR
    def x(self):
        return self._x or 0

    @x.setter  
    def x(self, value): ### MODIFICAR O METODO COMO SE FOSSE UM ATRIBUTO
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 100 ## USANDO O SETTER PARA MODIFICAR O VALOR
print(foo.x) 