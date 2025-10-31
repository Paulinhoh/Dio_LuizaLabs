'''
    O que são funções?
      Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros,
    esses parâmetros podem ou não ter valores padrão. Usar funções torna o código mais legível
    e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer
    que estamos programando de maneira estruturada.
'''


def exibir_mensagem():
    print('hello world!')


def exibir_mensagem2(nome):
    print(f'Seja bem vindo(a) {nome}!')


def exibir_mensagem3(nome='Anonimo'):
    print(f'Seja bem vindo(a) {nome}!')


exibir_mensagem()
exibir_mensagem2(nome='João')
exibir_mensagem3()
exibir_mensagem3(nome='Pedro')

'''
    Retornando valores
      Para retornar um valor, utilizamos a palavra reservada return. Toda função em Python retorna None por padrão,
    diferente de outras linguagens de programação, em python uma função pode retornar mais de um valor.
'''


def somar(numeros):
    return sum(numeros)


def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


print(somar([10, 20, 34]))  # Retorna 64
print(retorna_antecessor_sucessor(10))
a, s = retorna_antecessor_sucessor(10)  # a = 9, s = 11
print(a)
print(s)

'''
    Argumentos nomeados e não nomeados
'''


def salvar_carro(marca, modelo, ano, placa):
    # salvar carro no banco de dados
    print(f'Carro salvo: {marca}/{modelo}/{ano}/{placa}')


salvar_carro('BMW', 'i13', 2020, 'ABC-1234')  # Argumentos não nomeados
salvar_carro(marca='BMW', modelo='i13', ano=2020, placa='ABC-1234')  # Argumentos nomeados
salvar_carro(**{'marca': 'BMW', 'modelo': 'i13', 'ano': 2020, 'placa': 'ABC-1234'})  # Desempacotamento de dicionário
print()

'''
    Args e kwargs
      Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*aegs e **kwargs),
    o método recebe valores como tupla e dicionario respectivamente.
'''


def exibir_poema(data_extenso, *versos, **autor):
    texto = '\n'.join(versos)
    meta_dados = '\n'.join(f'{chave.title()}: {valor}' for chave, valor in autor.items())
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)


exibir_poema(
    '27 de março de 2024',
    'Eu gosto de programar em Python,',
    'É uma linguagem muito versátil,',
    'E com ela eu posso fazer muitas coisas!',
    autor='João Silva',
    cidade='São Paulo',
    ano=2020
)
