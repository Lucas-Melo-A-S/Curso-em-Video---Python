c=0
while True:
    print('-'*40)
    t=int(input('Qual a tabuada que você deseja saber: '))
    print('-' * 40)
    if t <= 0:
        break
    while c <= 9:
        c+=1
        print(f'{t} x {c} = {t*c}')
    c=0
print('FIM DO PROGRAMA')
