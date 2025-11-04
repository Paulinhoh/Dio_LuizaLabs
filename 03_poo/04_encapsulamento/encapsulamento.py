# =-=-=-=-=-=-=-=-= Recursos publicos e privados =-=-=-=-=-=-=-=-=
'''
    _nome_da_variavel -> colocar _ é uma convenção em ppython para demonstrar que é um atributo privado.
'''


class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        ...
        self._saldo += valor

    def sacar(self, valor):
        ...
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta(100)
conta.depositar(100)
conta.sacar(40)

print(conta.mostrar_saldo())


# =-=-=-=-=-=-=-=-= Propriedades =-=-=-=-=-=-=-=-=
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)

del foo.x
print(foo.x)


class Pessoa():
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property  # como se fosse um getter
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

    @nome.setter  # setter
    def nome(self, valor):
        self._nome = valor


pessoa = Pessoa('Paulo H', 2001)
print(f'Nome: {pessoa.nome}\tIdade: {pessoa.idade}')
pessoa.nome = 'Paulinho'
print(f'Nome: {pessoa.nome}\tIdade: {pessoa.idade}')
