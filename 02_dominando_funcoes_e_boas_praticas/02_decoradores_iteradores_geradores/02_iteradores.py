'''
    Iteradores
      Em python, um iterador é um objeto que contém um número contavel de valores que podem ser iterados, o que significa
    que você pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de um
    objeto, que consiste em dois métodos especiais "__iter__()" e "__next__()".
'''
from warnings import catch_warnings

'''
    Usos:
        * ler arquivos grandes
            * economiza memória evitando carregar todas as linhas do arquivo.
            * iterar linha a linha do arquivo.
'''


class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)
