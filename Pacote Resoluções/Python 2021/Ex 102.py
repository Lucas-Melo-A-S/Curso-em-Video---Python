def fatorial (numero=1,show=True):
    """
    O programa tem o objetivo de mostrar o valor do fatorial escolhido
    :param numero: Fatorial
    :param show: Se quer mostrar ou não o procedimento.
    :return: O valor final da fatoração
    """
    if show == False:
        for c in range (numero,1,-1):
            numero*=c
        return(numero)
    else:
        for c in range (numero,0,-1):
            numero*=c
            if c > 1:
                print(f'{c} x ', end = ' ')
            else:
                print(f'{c} =',end=' ')
        return(numero)


r=int(input('Qual o fatorial que você deseja calcular: '))
p1=str(input('Você deseja visualizar o processo na tela? [S/N]').upper())
p=p1[0]
if p == 'S':
    p = True
elif p == 'N':
    p=False
print(fatorial(r,p))


