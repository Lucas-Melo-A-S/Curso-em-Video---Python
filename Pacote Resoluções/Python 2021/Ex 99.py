from time import sleep
def maior(*lst):
    print('-='*30)
    print('Analisando os valores passados...')
    for c in lst:
        print (c,end = ' ')
        sleep(0.4)
    print(f'Foram analisados {len(lst)} valores ao todo!')
    print(f'O maior da lista é {max(lst)}')

maior(0,2,6,8,4,9)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
#list=[]
#while True:
#    a=int(input('Digite quantos numeros você quiser...Para sair digite 00: '))
#    if a == 00:
#        break
#    else:
#        list.append(a)
#        print('Numero Adicionado')
#maior(list)

