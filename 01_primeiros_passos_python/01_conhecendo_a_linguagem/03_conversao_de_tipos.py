'''
      Convertendo tipos

    Em alguns momentos é necessario ou sera necessario converter o tipo de uma variavel para manipular de forma diferente. Por exemplo:
        variaveis do tipo string, que armazenam números e precisamos fazer alguma operação matematica com esse valor.
'''

# inteiro para float
preco = 10
print(preco) # 10

preco = float(preco)
print(preco) # 10.0

preco = 10/2
print(preco) # 5.0


# float para inteiro
preco = 10.30
print(preco) # 10.3

preco = int(preco)
print(preco) # 10


# conversão por divisão
preco = 10
print(preco) # 10

print(preco / 2) # 5.0
print(preco // 2) # 5


# numerico para string
preco = 10.50
idade = 28
print(str(preco)) # 10.5
print(str(idade)) # 28

texto = f'idade {idade} preço {preco}'
print(texto) # idade 28 preço 10.5

