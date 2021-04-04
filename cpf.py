import time
from random import randint
import sys


def entrada_dados():
    cpf = input('\nInforme o CPF - ex.12345678901 : ')

    return cpf


def valida_cpf(cpf):
    if len(cpf) != 11:
        return False
    if cpf[0] * 11 in cpf:
        return False
    if not cpf.isdigit():
        return False

    return True


def calcula_digito(cpf):

    for i in range(2):
        print(f'\nCalculando o dígito {i + 1} : ')
        update_progress()
        soma = 0

        for contador, indice_cpf in enumerate(reversed(cpf), start=2):
            soma += contador * int(indice_cpf)

        digito = 11 - (soma % 11)

        if digito > 9:
            digito = 0

        cpf += str(digito)

    return cpf


def formatador_cpf(cpf):
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def gerador_cpf():
    print('\nGerando dígitos')
    update_progress()
    cpf_temp = ''.join([str(randint(0, 9)) for x in range(9)])
    cpf_temp = calcula_digito(cpf_temp)

    print(f'\n\nCPF gerado: {formatador_cpf(cpf_temp)}\n')


def validador_cpf():
    while True:
        input_cpf = entrada_dados()

        if not valida_cpf(input_cpf):
            print('\nCPF informado inválido!\nTente novamente.')
        else:
            break

    cpf_temp = input_cpf[:-2]
    cpf_temp = calcula_digito(cpf_temp)

    if cpf_temp == input_cpf:
        print('\n\nCPF Válido!\n')
    else:
        print('\n\nCPF Inválido!\n')


def update_progress():
    for i in range(101):
        time.sleep(0.04)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()


    













