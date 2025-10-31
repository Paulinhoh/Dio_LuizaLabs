def formatar_mensagem(texto):
    # Remove espaços extras do início e do fim da string
    texto = texto.strip()
    
    # TODO: Se a string ficou vazia após o strip, retorne a string vazia
    # Dica: verifique se o texto ficou vazio após retirar espaços
    
    # TODO: Processar o texto para garantir:
    #   - letras minúsculas
    #   - apenas um espaço separando as palavras (não podem haver múltiplos espaços)
    # Dica: separe a string em palavras e depois una novamente, garantindo um espaço entre elas
    palavras = texto.split()
    texto = ' '.join(palavras).strip().lower()

    
    # Retorne o texto já formatado conforme as regras
    # return mensagem_formatada
    return texto

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)
