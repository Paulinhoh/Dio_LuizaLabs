import sys


def main():
    # =-=-=-=-=-=-=-=-=-=-=--=-=- Estruturas Condicionais =-=-=-=-=-=-=-=-=-=-=--=-=-
    # Exemplo 1 (if/elif/else):
    opcao = int(input('Informe uma opção: \n[1] sacar \n[2] depositar \n-> '))

    if opcao == 1:
        print('Saque efetuado com sucesso!')
    elif opcao == 2:
        print('Depósito efetuado com sucesso!')
    else:
        sys.exit('Opção inválida!')

    # Exemplo 2 (if's aninhados):
    tipo_conta = 'universitaria'
    saldo = 500
    cheque_especial = 100
    saque = int(input('Informe o valor do saque: '))

    if tipo_conta == 'normal':
        if saldo >= saque:
            print('Saque efetuado com sucesso!')
        elif saque <= (saldo + cheque_especial):
            print('Saque efetuado com uso do cheque especial!')
        else:
            print('Saldo insuficiente!')
    elif tipo_conta == 'universitaria':
        if saldo >= saque:
            print('Saque efetuado com sucesso!')
        else:
            print('Saldo insuficiente!')
    else:
        print('O sistema não reconhece o tipo de conta! Entre em contato com o seu gerente.')

    # Exemplo 3 (operador ternário):
    status = 'Sucesso' if saldo >= saque else 'Falha'
    print(f'{status} ao realizar o saque!')

    # =-=-=-=-=-=-=-=-=-=-=--=-=- Estruturas de Repetição =-=-=-=-=-=-=-=-=-=-=--=-=-
    # for
    texto = 'Python'
    VOGAIS = 'aeiou'

    for letra in texto:
        if letra.lower() in VOGAIS:
            print(letra, end='')
    else:
        print()  # Quebra de linha -> sera executado apos o for terminar

    for indice in range(0, 11, 2):
        print(f'numeros pares de 0 à 10: {indice}', end=' ')

    # while
    opcao = -1
    while opcao != 0:
        opcao = int(input('\nInforme uma opção: \n[1] sacar \n[2] depositar \n[0] sair \n-> '))
        if opcao == 1:
            print('Saque efetuado com sucesso!')
        elif opcao == 2:
            print('Depósito efetuado com sucesso!')
        elif opcao == 0:
            print('Saindo...')
        else:
            print('Opção inválida! Tente novamente.')
            continue

    while True:
        senha = int(input('Informe sua senha (1234 para sair): '))
        if senha == 1234:
            print('Acesso permitido!')
            break
        else:
            print('Senha incorreta! Tente novamente.')
            continue

    # match
    opcao = 1
    match (opcao):
        case 1:
            print('Saque efetuado com sucesso!')
        case 2:
            print('Depósito efetuado com sucesso!')
        case _:
            print('Opção inválida!')


if __name__ == '__main__':
    main()
