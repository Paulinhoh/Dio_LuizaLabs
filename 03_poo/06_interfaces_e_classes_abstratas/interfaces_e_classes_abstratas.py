# =-=-=-=-=-=-=-=-= Variaveis de classe e variaveis de instancia =-=-=-=-=-=-=-=-=
from abc import abstractmethod, ABC, abstractproperty
from idlelib.debugobj_r import remote_object_tree_item


class Estudante:
    _escola = 'DIO'  # variavel de classe

    def __init__(self, nome, matricula):
        self._nome = nome  # variavel de instancia
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula

    @property
    def escola(self):
        return self._escola

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @escola.setter
    def escola(self, escola):
        self._escola = escola

    def __str__(self):
        return f'Estudante: {self._nome},\tMatricula: {self._matricula},\tEscola: {self._escola}'


print('=-' * 30)
aluno_1 = Estudante('Aluno 1', 1)
aluno_2 = Estudante('Aluno 2', 2)

print(aluno_1)
print(aluno_2)
print()

aluno_1.matricula = 3
aluno_1 = Estudante('Aluno 1', 1)
aluno_2 = Estudante('Aluno 2', 2)
print(aluno_1)
print(aluno_2)
print()

Estudante._escola = 'Curso em Video'
print(aluno_1)
print(aluno_2)
print('=-' * 30)

# =-=-=-=-=-=-=-=-= Métodos de classe e métodos estáticos =-=-=-=-=-=-=-=-=
'''
    Métodos de Classe:
      Métodos de classe estão ligados à classe e não ao objeto. Eles tem acesso ao estado da classe, pois
    recebem um parêmetro que aponta para a classe e não para a instância do objeto.
    
    Métodos estáticos:
      Um método estatico não recebe um primeiro argumento explicito. Ele também é um método vinculado à classe e 
    não ao objeto da classe. Este está presente em uma classe porque faz sentido que o método esteja presente na 
    classe.
    
    Métodos de classe x Métodos estáticos:
      * Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estatico não.
      * Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessa-lo
      ou modifica-lo
    
    Quando utilizar método de classe ou estático:
      * Geralmente usamos o método de classe para criar métodos de fábrica.
      * Geralmente usamos métodos estáticos para criar funções utilitárias.
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # método de class
    def retornar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod  # método estático
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.retornar_apartir_data_nascimento(2001, 7, 31, 'Paulo H')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))
print('=-' * 30)

# =-=-=-=-=-=-=-=-= O que são interfaces =-=-=-=-=-=-=-=-=
'''
    O que são interfaces:
      Interfaces definem o que uma classe deve fazer e não como.
      
    Python tem interfaces?
      O conceito de interfaces é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas
    respectivas assinaturas. Em python utilizamos classes abstratas para criar contratos. Classes abstratas não 
    podem ser instanciadas. 
'''

# =-=-=-=-=-=-=-=-= Classes abstratas =-=-=-=-=-=-=-=-=
'''
    Criando classes abstratas com o módulo abc
    
    ABC:
      Por padrão, o python não fornece classes abstratas. O python vem com um módulo que fornece a base para definir 
    as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, 
    em seguida, registrando classes concretas como implemetações da base abstrata. Um método se torna abstrato quando 
    decorado com @abstractmethod. 
'''


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # propriedade abstrata
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('Ligado!')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligado!')

    @property
    def marca(self):
        return 'LG'


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o ArCondicionado...')
        print('Ligado!')

    def desligar(self):
        print('Desligando o ArCondicionado...')
        print('Desligado!')

    @property
    def marca(self):
        return 'SAMSUMG'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
print()

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)
print('=-' * 30)
