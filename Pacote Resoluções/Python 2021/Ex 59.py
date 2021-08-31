n1=float(input('Digite um valor: '))
n2=float(input('Digite mais um valor: '))
while True:
    c=int(input('''Você deseja realizxar qual das opções:
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do programa
    : '''))
    if c == 1:
        print(f'A soma dos valores é  {n1+n2}')
    elif c == 2:
        print(f'A multiplicação dos valores é {n1*n2}')
    elif c ==3:
        print(f'O maior valor é {max(n1,n2)}')
    elif c == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite mais um valor: '))
    elif c == 5:
        break
    else:
        print('OPÇÃO INVALIDA...TENTE NOVAMENTE')
print('Fim')
