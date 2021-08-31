def area(largura,comprimento):
    print('Controle de terreno')
    print('-'*20)
    a=largura * comprimento
    print(f'A lagura do terreno é {largura} e o comprimento é {comprimento}')
    print(f'A área do terreno é {a}')


l=float(input('Largura (m): '))
c=float(input('O Comprimento (m): '))
area(l,c)