'''
    O que são geradores?
      São tipos especiais de iteradores, ao contrario das listas ou outros iteraveis, não armazenam
    todos os seus valores na memória.
      São definidos usando funções regulares, mas, ao invés de retornar valores usando "retrun", utilizam "yield".

    Caracteristicas de geradores:
        * Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.
        * O estado interno de um gerador é mantido entre chamadas.
        * A execução de um gerador é pausada na declaração "yield" e retomada daí na proxima vez que ele for chamado.
'''

'''
    Exemplo --> Recuperando dados de uma API:
        * solicitar dados por página (paginação).
        * fornecer um produto por vez entre as chamadas.
        * quando todos os produtos de uma pagína forem retornados, verificar se existem novas páginas.
        * tratar o consumo da API como uma lista Python.
'''
import requests


def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f'{api_url}?page={page}')
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1


# Uso do gerador
for product in fetch_products('http://api.example.com/products'):
    print(product['name'])


# exemplo simples
def meu_gerador(numeros: list[int], contador=0):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numero=[1, 2, 3]):
    print(i)

'''
    Se usa geradores quando o código for simples.
'''
