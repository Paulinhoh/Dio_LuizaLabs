'''
      O que são variaveis e constantes?

    Variaveis: em liguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variaveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução de programa.

    Constantes: assim como as variaveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutavel.

      Python não tem constantes:
    Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
    Em Python usamos a convenção que diz ao programador que a variavel é uma constante. Para fazer isso, você deve criar a variavel com o nome todo em letras maiusculas

      Boas práticas
    * O padrão de nomes deve ser snake case.
    * Escolher nomes sugestivos.
    * Nome de constantes todo em maiusculo.
'''

# exemplo variaveis
age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.') # Meu nome é Guilherme e eu tenho 23 ano(s) de idade.

age, name = (27, 'Giovanna')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.') # Meu nome é Giovanna e eu tenho 27 ano(s) de idade.

# exemplo constantes
ABS_PATH = 'C:\\Users\\Paulo Henrique\\github'
DEBUG = True
STATES = [
    'SP', 
    'RJ', 
    'MG',
]
AMOUNT = 32.2
