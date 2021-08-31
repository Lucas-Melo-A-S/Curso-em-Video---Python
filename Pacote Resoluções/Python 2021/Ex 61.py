print('GERADOR DE PA')
print('=-'*20)
pt=int(input('Digite o primeiro numero da PA: '))
r=int(input('Digite a razão da PA: '))
x=0
print(pt, end='...')
print('=-'*20)
while x<9:
    x+=1
    pt+=r
    print(pt,end='...')