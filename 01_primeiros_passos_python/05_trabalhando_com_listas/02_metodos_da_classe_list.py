lista = []

# .append() - Adiciona um elemento ao final da lista
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)  # [1, 'Python', [40, 30, 20]]
print()

# .clear() - Remove todos os elementos da lista
lista.clear()
print(lista)  # []
print()

lista.append(5)

# .copy() - Retorna uma cópia rasa da lista
l2 = lista.copy()
print(l2)  # [5]
print(id(lista), id(l2))  # IDs diferentes

# .count() - Retorna o número de ocorrências de um elemento na lista
lista.append(5)
lista.append(88)

print(lista.count(88))  # 1
print(lista.count(5))  # 2

# .extend() - Adiciona os elementos de um iterável ao final da lista
l2.append('Python')
lista.extend(l2)
lista.extend([22, 'java'])
print(lista)  # [5, 5, 88, 5, 'Python', 22, 'java']
print()

# .index() - Retorna o índice da primeira ocorrência de um elemento na lista
print(lista.index('java'))  # 6

# .pop() - Remove e retorna o elemento no índice especificado (último por padrão)
lista.pop()  # 'java'
lista.pop()  # 22
lista.pop(0)  # 5
print(lista)  # [5, 88, 5, 'Python']
print()

# .remove() - Remove a primeira ocorrência de um elemento na lista
lista.remove(5)
print(lista)  # [88, 5, 'Python']

# .reverse() - Inverte a ordem dos elementos na lista
lista.reverse()
print(lista)  # ['Python', 5, 88]
print()

# .sort() - Ordena os elementos da lista (somente elementos comparáveis)
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort()  # ['c', 'csharp', 'java', 'js', 'python']

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(reverse=True)  # ['python', 'js', 'java', 'csharp', 'c']

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x))  # ['c', 'js', 'java', 'python', 'csharp']

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x), reverse=True)  # ['python', 'csharp', 'java', 'js', 'c']

# .len() - Retorna o tamanho da lista
print(len(linguagens))  # 5

# sorted() - Retorna uma nova lista ordenada a partir de um iterável
numeros = [6, 1, 8, 2, 4]
sorted(numeros)  # [1, 2, 4, 6, 8]
sorted(numeros, reverse=True)  # [8, 6, 4, 2, 1]
