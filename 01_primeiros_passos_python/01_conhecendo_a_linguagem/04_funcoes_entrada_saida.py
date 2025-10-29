'''
      Lendo dados com a função Input
    Função input: a função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuario na saida padrão (tela). A função lê a entrada, coverte para string e retorna o valor.

      Exibindo valores com a função Print
    Função print: a função builtin print é utilizada quando queremos exibir dados na saida padrão (tela).  Ela recebe um argumento obrigatorio do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string fianl é exibida para o usuário.
'''

# exemplo input
nome = input('Informe o seu nome: ') # Informe o seu nome: 

# exemplo print
nome = 'Paulo Henrique'
sobrenome = 'Reis'

print(nome, sobrenome) # Paulo Henrique Reis
print(nome, sobrenome, end='...\n') # Paulo Henrique Reis...
print(nome, sobrenome, sep='#') # Paulo Henrique#Reis
