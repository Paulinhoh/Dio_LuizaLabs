# -=-=-=-===-=-=-=-=-=-=--= Operadores Aritméticos -=-=-==--=-=-=-=-=-=-
'''
    +  -> Adição
    -  -> Subtração
    *  -> Multiplicação
    /  -> Divisão
    // -> Divisão Inteira
    %  -> Módulo (Resto da Divisão)
    ** -> Exponenciação
'''

# adição
print(1 + 1)  # 2

# subtração
print(5 - 2)  # 3

# multiplicação
print(3 * 4)  # 12

# divisão
print(10 / 2)  # 5.0

# divisão inteira
print(10 // 3)  # 3

# módulo (resto da divisão)
print(10 % 3)  # 1

# exponenciação
print(2 ** 3)  # 8

# Precendencia dos operadores  -> () -> ** -> * / // % -> + -
print()

# -=-=-=-===-=-=-=-=-=-=--= Operadores de Comparação -=-=-==--=-=-=-=-=-=-
'''
    ==  -> Igual a
    !=  -> Diferente de
    >   -> Maior que
    <   -> Menor que
    >=  -> Maior ou igual a
    <=  -> Menor ou igual a
'''

saldo = 200
saque = 200

print(saldo == saque)  # True
print(saldo != saque)  # False
print(saldo > saque)  # False
print(saldo < saque)  # False
print(saldo >= saque)  # True
print(saldo <= saque)  # True
print()

# -=-=-=-===-=-=-=-=-=-=--= Operadores de Atribuição -=-=-==--=-=-=-=-=-=-
'''
    =  -> Atribuição Simples
    += -> Atribuição de Adição
    -= -> Atribuição de Subtração
    *= -> Atribuição de Multiplicação
    /= -> Atribuição de Divisão
    //=-> Atribuição de Divisão Inteira
    %= -> Atribuição de Módulo
    **=-> Atribuição de Exponenciação
'''

# -=-=-=-===-=-=-=-=-=-=--= Operadores Lógicos -=-=-==--=-=-=-=-=-=-
'''
    and  -> E
    or   -> Ou
    not  -> Não
'''

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)  # False
print(saldo >= saque or saque <= limite)  # True
print(not (saldo >= saque))  # False
print()

# -=-=-=-===-=-=-=-=-=-=--= Operadores de Identidade -=-=-==--=-=-=-=-=-=-
'''
      Compara se ocupam o mesmo espaço na memória.
    is  -> É o mesmo que
    is not -> Não é o mesmo que
'''

# -=-=-=-===-=-=-=-=-=-=--= Operadores de Associação -=-=-==--=-=-=-=-=-=-
'''
     São operadores que verificam se um valor faz parte de uma sequência.
    in  -> Está em
    not in -> Não está em
'''

curso = 'Curso de Python'
frutas = ['banana', 'maçã', 'laranja']
saques = [1500, 100]

print('Python' in curso)  # True
print('uva' not in frutas)  # True
print(200 in saques)  # False
print()
