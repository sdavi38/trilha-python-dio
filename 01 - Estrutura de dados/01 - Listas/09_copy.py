## Metodo copy ==> uma lista em uma estancia diferente
# mantendo a lista original ##

lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

lista2.append("David")
lista2[0]="Aba"
print(lista2)

#print((id(lista2), id(lista)))