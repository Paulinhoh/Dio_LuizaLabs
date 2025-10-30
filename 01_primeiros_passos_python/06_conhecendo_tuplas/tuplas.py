# tuplas são imutáveis, ou seja, não podem ser alteradas após a criação
# são definidas por parênteses ()
# podem conter elementos de tipos diferentes

# criando tuplas
frutas = ("laranja", "pera", "uva",)
letras = tuple('python')
numero = tuple([1, 2, 3, 4])
pais = ('Brasil',)

# assessando elementos
print(frutas[0])  # laranja
print(frutas[-1])  # uva

# tuplas aninhadas (matrix)
matrix = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c')
)
print(matrix[0])  # [1, 'a', 2]
print(matrix[0][1])  # 'a'
print(matrix[2][2])  # 'c'
print(matrix[-1][-1])  # 'c
print()

# fatiamento de tuplas (slicing)
# mesma lógica das listas

# iterar tuplas
# mesma lógica das listas

# métodos de tuplas
'''
    .count()    - conta quantas vezes um elemento aparece na tupla
    .index()    - retorna o índice da primeira ocorrência de um elemento na tupla
    .len()      - retorna o tamanho da tupla
'''
