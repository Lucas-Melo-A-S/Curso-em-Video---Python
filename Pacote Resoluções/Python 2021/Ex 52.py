n=int(input('Digite um numero: '))
t=0
for c in range(1,n+1):
    if n%c==0:
        t+=1
if t==2:
    print('Esse numero é primo, ele foi dividod somente por ele e por um')
else:
    print(f'Esse numero não é primo, ele foi dividido {t} vezes')

