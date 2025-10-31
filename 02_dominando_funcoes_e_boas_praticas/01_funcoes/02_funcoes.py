'''
    Parametros especiais
    - \ : Parametros apenas posicionais (antes da \)
    - * : Parametros apenas nomeados (keyword only) (depois do *)
'''


def criar_carro(modelo, ano, placa, /, marca, motor):
    print(modelo, ano, placa, marca, motor)


# criar_carro(modelo='Gol', ano=2020, placa='ABC-1234', marca='Volkswagen', motor='1.0') # invalido
criar_carro('Gol', 2020, 'ABC-1234', marca='Volkswagen', motor='1.0')  # valido


def criar_carro2(*, modelo, ano, placa, marca, motor):
    print(modelo, ano, placa, marca, motor)


# criar_carro2('Gol', 2020, 'ABC-1234', marca='Volkswagen', motor='1.0') # invalido
criar_carro2(modelo='Gol', ano=2020, placa='ABC-1234', marca='Volkswagen', motor='1.0')  # valido

'''
    Objetos de primeira classe
      Em python tudo é objeto, dessa forma funções també são objetos o que as tornam objetos de primeira classe. Com 
    isso podemos atribuir funções a variaveis, passa-las como parametro para funções, usa-las como valores em estruturas
    de dados (listas, tuplas, dicionarios, etc) e até mesmo criar funções que retornam outras funções.
'''


def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado é: {resultado}')


exibir_resultado(10, 10, somar)

# escopo (local, global)
salario = 2000


def salario_bonus(bonus):
    global salario  # acessa a variavel global
    salario += bonus
    return salario


print(salario_bonus(500))
