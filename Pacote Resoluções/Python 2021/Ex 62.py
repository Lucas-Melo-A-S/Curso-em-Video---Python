pt=int(input('Digite o primeiro numero da PA: '))
r=int(input('Digite a razão da PA: '))
x=1
print(pt, end='...')
while x<10:
    x+=1
    pt+=r
    print(pt,end='...')
print('Pausa')
y=str(input('\nVocê deseja continuar? [S/N]: ').upper())
while y=='S':
    w=0
    c=int(input('Você quer mais qunatos termos: '))
    while w<c:
        pt += r
        w+=1
        x+=1
        print(pt, end='...')
    print('Pausa')
    y = str(input('\nVocê deseja continuar? [S/N]: ').upper())
print(f'A progressão foi finalizada com {x} termos')