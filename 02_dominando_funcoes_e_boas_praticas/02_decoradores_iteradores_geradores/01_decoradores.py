# primeiro decorador
import functools


def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a função.')
        funcao()
        print('Faz algo depois de executar a função.')

    return envelope


def ola_mundo():
    print('Olá mundo!')


ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
print()


# Açucar sintático!
# O python permite que você use decoradores de maneira mais simples com o simbolo @.

@meu_decorador
def ola_mundo2():
    print('Olá mundo!')


ola_mundo2()
print()


# funções de decoradores com argumentos (*args e **kwargs)
def meu_decorador2(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar a função.')
        funcao(*args, **kwargs)
        print('Faz algo depois de executar a função.')

    return envelope


@meu_decorador2
def ola_mundo3(nome):
    print(f'Olá mundo!, {nome}')


ola_mundo3('Camille')
print()


# retornando valores de funções decoradas
def meu_decorador3(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar a função.')
        resultado = funcao(*args, **kwargs)
        print('Faz algo depois de executar a função.')
        return resultado

    return envelope


@meu_decorador3
def ola_mundo4(nome):
    print(f'Olá mundo!, {nome}')
    return nome.upper()


resultado = ola_mundo4('Camille')
print(resultado)
print()


# introspecção: é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução.
def meu_decorador4(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope


@meu_decorador4
def ola_mundo5(nome):
    print(f'Olá mundo!, {nome}')


print(ola_mundo5.__name__)
