# criação de um dicionário
pessoa = {'nome': 'João', 'idade': 30}
pessoa = dict(nome='João', idade=30)

pessoa['telefone'] = '1234-5678'  # adiciona um novo par chave-valor

pessoa['nome'] = 'Maria'  # atualiza o valor da chave 'nome'
pessoa['idade'] = 28

print(pessoa)

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 30, 'telefone': '9876-5432'},
    'maria@gmail.com': {'nome': 'Maria', 'idade': 28, 'telefone': '1234-5678'}
}

print(contatos['maria@gmail.com']['telefone'])  # acessa o telefone de Maria

# iterando sobre um dicionário
for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')
print()

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
print()
