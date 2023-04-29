def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam



def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho(('MENU PRINCIPAL'))
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
