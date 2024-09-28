# Filtrar lista
numeros = [0, 3, 22, 15, 40, 56, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
          ###lista interação e if e se atender a condição##
print(pares)
print(impares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
