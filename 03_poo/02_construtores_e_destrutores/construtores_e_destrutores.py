class Cachorro:
    def __init__(self, nome, cor, acordado=True):  # construtor
        print('Iniciando a classe Cachorro...')

        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):  # destrutor
        print('Destruindo a classe Cachorro...')

    def falar(self):
        print('auau...')


c = Cachorro('Husky', 'branco')
c.falar()
c.falar()

print('ola, mundo')
del c
print('ola, mundo')
print('ola, mundo')
print('ola, mundo')
