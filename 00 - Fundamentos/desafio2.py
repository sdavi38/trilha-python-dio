def analise_vendas(vendas):
    
    total_vendas = sum(vendas)
    qtd_vendas= len(vendas)
    media_vendas = total_vendas / qtd_vendas
     
     
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    
  entrada = input().split(',')
  
  vendas = list(map(int, entrada))
   
    
  return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))