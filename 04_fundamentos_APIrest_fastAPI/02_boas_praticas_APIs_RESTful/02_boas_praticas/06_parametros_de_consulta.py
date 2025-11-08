"""
6 -> Parâmetros de Consulta
O que são Parâmetros de Consulta?
  Parâmetros de consulta (ou query parameters) são parte de uma URL (Uniform Resource Locator) que permite que informações adicionais sejam enviadas para um servidor. Eles são usados para filtrar, paginar, e ordenar dados, entre outras funções. Esses parâmetros são anexados à URL após um ponto de interrogação (?), e múltiplos parâmetros são separados por um e comercial (&).


Analogia:
  Imagine que você está em uma livraria online procurando por livros. A livraria tem milhares de livros, mas você está interessado apenas em livros de ficção científica que custam menos de R$50. Em vez de olhar cada página do catálogo, você pode usar filtros na pesquisa para encontrar exatamente o que deseja. Esses filtros são como parâmetros de consulta que você adiciona para refinar sua pesquisa.
"""

# Exemplo pratico:
url = "https://exemplo.com/products"
params = {"category": "eletronics", "limit": 10, "page": 1, "sort": "price"}

response = requests.get(url, params=params)  # type: ignore
print(response.json())

# Aqui, a biblioteca requests simplifica o processo de adicionar parâmetros de consulta à URL. Você define um dicionário params, e o requests cuida do resto.


"""
Como funciona os parametros de consulta?
    * Filtro: Parâmetros como category=electronics permitem que você filtre os resultados para mostrar apenas os produtos da categoria "eletrônicos".
    * Limite (Pagination): Parâmetros como limit=10 controlam o número de resultados retornados. Por exemplo, limit=10 significa que você só quer 10 produtos por página.
    * Paginação: Parâmetros como page=1 indicam em qual página você está navegando. Se houver muitas páginas, você pode mudar para page=2, page=3, etc.
    * Ordenação: Parâmetros como sort=price ordenam os resultados com base em um critério, como o preço.


Comparação com uma situação real:
  Imagine que você vai a um supermercado (equivalente a acessar um site). Ao invés de procurar produto por produto nas prateleiras (equivalente a visualizar todas as páginas sem filtro), você pede ao atendente (equivalente ao servidor) que mostre apenas os itens da seção de eletrônicos, que custem até R$50, e que estejam na promoção. Os parâmetros de consulta funcionam como esses filtros que você pediu.
"""
