import cpf

while True:
    print('PROGRAMA CPF'.center(40, '-'))
    print('\n1 - Validar CPF')
    print('2 - Gerar CPF')
    print('0 - Sair do programa')

    opcao = input('Escolha sua opção: ')

    if opcao == '1':
        cpf.validador_cpf()
    elif opcao == '2':
        cpf.gerador_cpf()
    elif opcao == '0':
        print('\nSaindo...\nObrigado por utilizar o programa.')
        break
    else:
        print('\nOpção inválida\nTente novamente.')


