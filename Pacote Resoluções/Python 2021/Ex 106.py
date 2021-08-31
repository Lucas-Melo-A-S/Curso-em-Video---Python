def ajuda(com):
    help(com)


def titulo(msg):
    print('~'*(len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


while True:
    titulo('Programa de ajuda python')
    c=str(input('Digite qual comando você deseja acessar: '))
    if c.upper() != 'FIM':
        ajuda(c)
    else:
        print('Programa encerrado')
        break
titulo('Até Logo')