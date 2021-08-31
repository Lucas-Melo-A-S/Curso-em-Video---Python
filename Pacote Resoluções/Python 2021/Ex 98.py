from time import sleep
def contador(inicio,fim,passo):
    print('-='*30)
    if passo < 0:
        passo=passo*(-1)
    elif passo == 0:
        passo = 1
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} a {passo}')
        print(inicio, end=' ')
        sleep(0.5)
        while inicio < fim:
            inicio+=passo
            if inicio <= fim:
                print(inicio,end=' ')
                sleep(0.5)
        print('\nContador finalizado')
    elif fim <= inicio:
        print(f'Contagem de {inicio} até {fim} de {passo} a {passo}')
        print(inicio, end=' ')
        sleep(0.5)
        while fim <= inicio:
            inicio-=passo
            if fim <= inicio:
                print(inicio,end=' ')
                sleep(0.5)
        print('\nContador finalizado')


contador(0,10,1)
contador(10,1,2)


i=int(input('Digite o valor de inicio: '))
f=int(input('Digitre o valor final: '))
p=int(input('Digite quantos passos será feito por vez: '))

contador(i,f,p)