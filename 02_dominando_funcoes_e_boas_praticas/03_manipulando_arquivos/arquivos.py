# =-=-=-=-=-=-=-=-= Introdução =-=-=-=-=-=-=-=-=
'''
    Por que precisamos manipular arquivos?
      Os arquivos são esseciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar dados.
    Através da manipulação de arquivos , podemos persistir os dados além da vida util de um programa especifico.

    Conceitos de arquivos em informatica:
      Um arquivo é um conteiner no computador onde as informações são armazenadas em formato digital. Existem dois tipos
    de arquivos que podemos manipular em python: arquivos de texto e arquivos binario.
'''
from traceback import print_tb

# abrindo e fechando arquivos
file = open('example.txt', 'r')  # abrindo o arquivo
# ... faz algo com o arquivo
file.close()  # fechando o arquivo -> muito importante sempre fechar o arquivo depois de utilizado

'''
    Modos de abertura:
    * r - leitua do arquivo
    * w - escrever no arquivo
    * a - anexar (colocar conteudo em um arquivo ja existente)
'''

# para ler um arquivo
file = open('example.txt', 'r')
file.close()

# para escrever em um arquivo
file = open('example.txt', 'w')
file.close()

# para anexar conteudo a um arquivo existente
file = open('example.txt', 'a')
file.close()

# =-=-=-=-=-=-=-=-= Lendo de um arquivo =-=-=-=-=-=-=-=-=
'''
    Python fornece varias maneiras de ler um arquivo. Podemos usar:
    * read()
    * readline()
    * readlines()
'''

# ler todo o conteudo do arquivo de uma vez
file = open('example.txt', 'r')
print(file.read())
file.close()

'''
    readline() -> lê uma linha por vez.
    readlines() -> retorna uma lista onde cada elemento é uma linha do arquivo.
'''

# dica
file = open('example.txt', 'r')
while (linha := len(file.readline())):
    print(linha)
file.close()

# =-=-=-=-=-=-=-=-= Escrevendo em um arrquivo =-=-=-=-=-=-=-=-=
arquivo = open('example.txt', 'w')
arquivo.write("Escrevendo dados em um arquivo.")  # escrve no arquivo
arquivo.writelines(['Escrevendo ', 'um\n', 'novo ', 'texto '])  # escrve no arquivo

arquivo.close()

# =-=-=-=-=-=-=-=-= Gerenciando arquivos e diretorios =-=-=-=-=-=-=-=-=
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # pega o path em que esta o arquivo

# cria um diretorio
os.mkdir("exemplo")

# renomeia um arquivo
os.rename('old.txt', 'new.txt')

# remover um arquivo
os.remove('unwanted.txt')

# mover um arquivo
shutil.move('source.txt', 'destination.txt')

# =-=-=-=-=-=-=-=-= Tratamento de exceções em manipulação de arquivos =-=-=-=-=-=-=-=-=
'''
    Exceções mais comuns:
    * FileNotFoundError -> lançada quando o arquivo que esta sendo aberto não pode ser encontrado no diretorio especifico.
    * PermissionError -> lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adquadas para leitura ou gravação.
    * IOError -> lançada quando ocorre um erro geral de E/S ao trabalhar com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros. 
    * UnicodeDecodeError -> lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
    * UnicodeEncodeError -> lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo.
    * IsADirectoryError -> lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.
    * OSError -> 
'''

try:
    arquivo = open('meu_aquivo.py')
except FileNotFoundError as err:
    print('Arquivo não encontrado')
    print(err)  # printa os detalhes da exceção
except IsADirectoryError as err:
    print(f'Não foi possivel abrir o arquivo: {err}')
except Exception as err:  # tratamento mais generico
    print(f'Algum problema ocorreu ao tentar abrir o arquivo: {err}')
arquivo.close()

# =-=-=-=-=-=-=-=-= Boas praticas na manipulação de arquivos =-=-=-=-=-=-=-=-=
with open('meu_aquivo.py', 'r') as arquivo:  # com o with o arquivo é fechado automaticamente
    print(arquivo.read())

# *verificar se o arquivo foi aberto com sucesso
try:
    with open('meu_aquivo.py', 'w', encoding='utf-8') as arquivo:
        ...
except IOError as err:
    print(f'Erro ao abrir o arquivo: {err}')

# =-=-=-=-=-=-=-=-= Trabalhando com arquivos CSV =-=-=-=-=-=-=-=-=
import csv

try:
    with open('meu_aquivo.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as err:
    print(f'Erro ao abrir o arquivo: {err}')

try:
    with open('meu_aquivo.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as err:
    print(f'Erro ao abrir o arquivo: {err}')
