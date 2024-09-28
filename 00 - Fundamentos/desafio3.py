def produto_mais_vendido(produtos):
    contagem = {}
    
    # Conta a ocorrência de cada produto
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    # Inicializa variáveis para armazenar o produto mais vendido
    max_produto = None
    max_count = 0
    
    # Encontra o produto com a maior contagem
    for produto, count in contagem.items():
        if count > max_count:
            max_produto = produto
            max_count = count
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Informe os produtos vendidos, separados por vírgula: ").split(',')
    
    # Remove espaços em branco extras de cada produto
    produtos = [produto.strip() for produto in entrada]
    
    return produtos

# Obtém a lista de produtos e exibe o produto mais vendido
produtos = obter_entrada_produtos()
print("Produto mais vendido:", produto_mais_vendido(produtos))
