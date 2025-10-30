# atribuições em listas
frutas = ['laranja', 'maça', 'uva']
print(frutas)

frutas = []
print(frutas)

letras = list('abcdefghijklmnopqrstuvwxyz')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 4_200_000, 2020, 2900, 'São Paulo', True]
print(carro)
print()

frutas = ['laranja', 'maça', 'uva', 'pera']
print(frutas[0])  # laranja
print(frutas[1])  # maça
print(frutas[-1])  # pera
print()

# listas aninhadas (matrix)
matrix = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matrix[0])  # [1, 'a', 2]
print(matrix[0][1])  # 'a'
print(matrix[2][2])  # 'c'
print(matrix[-1][-1])  # 'c
print()

# fatiamento de listas (slicing)
letras = ['p', 'y', 't', 'h', 'o', 'n']
print(letras[2:])  # ['t', 'h', 'o', 'n']
print(letras[:2])  # ['p', 'y']
print(letras[1:3])  # ['y', 't']
print(letras[0:3:2])  # ['p', 't']
print(letras[::])  # ['p', 'y', 't', 'h', 'o', 'n']
print(letras[::-1])  # ['n', 'o', 'h', 't', 'y', 'p']
print()

# iterar listas
carros = ['Ferrari', 'BMW', 'Audi']

for carro in carros:
    print(carro, end=' ')  # Ferrari BMW Audi
print()

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')
    # 0: Ferrari
    # 1: BMW
    # 2: Audi
print()

# compreensão de listas
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)  # [30, 2, 34]

pares_compreensao = [numero for numero in numeros if numero % 2 == 0]
print(pares_compreensao)  # [30, 2, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado) # [1, 900, 441, 4, 81, 4225, 1156]
print()
