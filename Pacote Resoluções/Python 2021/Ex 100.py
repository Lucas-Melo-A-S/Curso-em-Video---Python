from random import randint
from time import sleep
list=[]
def sorteia(lst):
    x=0
    i=0
    print(f'Sorteando os 5 valores da lista: ', end=' ')
    sleep(0.6)
    while x <= 4:
        a=randint(0,10)
        lst.append(a)
        print(lst[i], end= ' ')
        sleep(0.6)
        x+=1
        i+=1

def épar(v):
    return v%2==0


def somapar(lst):
    s=0
    for e,v in enumerate(lst):
        if épar(v):
            s+=v
    print(f'\nA soma dos valores Par da lista {lst}, é {s}')

sorteia(list)
somapar(list)
