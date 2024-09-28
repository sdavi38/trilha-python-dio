

### Classes:definir as caracteristas e comportamento de um 
## objeto e são abstratas. Objetos: Possuem caracteristicas e 
## comportamentos que forma definidos nas classes.É são utilizados.
class Bicicleta:
    
    ##Construtor >>> Self é a referencia do objeto
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        
        print("Vrummmmm...")

    ##DEFINIR OS ATRIBUTOS DA CLASSE
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

### INSTANCIANDO  A CLASS   
b1 = Bicicleta("vermelha", "caloi", 2022, 600,22)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189,18)
print(b2)
b2.correr()
##TRIBUTOS SÃO ACESSADOS PUBLICAMENTE
print (b1)
