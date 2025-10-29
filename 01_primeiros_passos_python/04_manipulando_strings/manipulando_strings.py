# -=-=-=-=-=-=-=-=-=-=--= Metodos uteis da classe string -=-=-=-=-=-=-=-=-=-=--=
curso = 'Curso de pYtHon'

print(curso.lower())  # curso de python
print(curso.upper())  # CURSO DE PYTHON
print(curso.title())  # Curso De Python
print(curso.capitalize())  # Curso de python

curso = '   Python   '
print(curso.strip())  # 'Python'
print(curso.lstrip())  # 'Python   '
print(curso.rstrip())  # '   Python'

curso = 'Python'
print(curso.center(10, '#'))  # ##Python##
print('.'.join(curso))  # P.y.t.h.o.n
print()

# -=-=-=-=-=-=-=-=-=-=--= Interpolação de variaveis -=-=-=-=-=-=-=-=-=-=--=
nome = 'Paulinho'
idade = 24
profissao = 'Programador'
linguagem = 'Python'

dados = {'nome': nome, 'idade': idade, 'profissao': profissao, 'linguagem': linguagem}

print('Olá, me chamo %s. Eu tenho %d anos, trabalho como %s e programo em %s.' % (nome, idade, profissao, linguagem))
print(
    'Olá, me chamo {}. Eu tenho {} anos, trabalho como {} e programo em {}.'.format(nome, idade, profissao, linguagem))
print('Olá, me chamo {3}. Eu tenho {2} anos, trabalho como {1} e programo em {0}.'.format(linguagem, profissao, idade,
                                                                                          nome))
print(
    'Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} e programo em {linguagem}.'.format(**dados))
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} e programo em {linguagem}.')
print()

PI = 3.14159
print(f'Valor de PI: {PI:.2f}')  # Valor de PI: 3.14
print(f'Valor de PI: {PI:10.2f}')  # Valor de PI:           3.14
print()

# -=-=-=-=-=-=-=-=-=-=--= Fatiando strings -=-=-=-=-=-=-=-=-=-=--=
nome = 'Paulo Henrique dos Santos Reis'
print(nome[0])  # P
print(nome[:5])  # Paulo
print(nome[6:])  # Henrique dos Santos Reis
print(nome[6:13])  # Henrique
print(nome[0:21:2])  # PloHnrid s atsRs
print(nome[::-1])  # sieR sotnaS sod euqnirH oluaP
print(nome[-1])  # s

# -=-=-=-=-=-=-=-=-=-=--= String multiplas linhas -=-=-=-=-=-=-=-=-=-=--=
'''
    comentarios de multiplas linhas
'''

"""
    outra forma de comentarios de multiplas linhas
"""

msg = '''
    string de multiplas linhas
'''

msg2 = """
    outra forma de string de multiplas linhas
"""
print('''
    -=-=-==--= Menu: -=-=-==--=
    
    [1] - popopopopopopo
    [2] - lklklklklklklk
    [3] - mkmkmkmkmkmkmk
    
    -=-=-==-=--=-=-=-=-=-=-=--=
            Ass: sdkadkoskdoads

''')
