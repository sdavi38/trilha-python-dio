###CRIA CHAVES SEM VALOR

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
resultado["nome"] = "David"
print(resultado)

###CRIA CHAVES COM VALOR
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
