## TUPLAS É MAIS RESTRITA QUE A TUPLA E IMUTAVÉL ##

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

frutas1 = tuple([
     "laranja",
    "pera",
    "uva",
])
print(frutas1)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) ##virgula no final para não confundir com operaçãop
print(pais)
