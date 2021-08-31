import math
p1=float(input('Qual a sua nota da P1?: '))
p2=float(input('Qual a sua nota da P2?: '))
pt=((p1+p2)/2)
if pt <= 5:
    print(f'Você está reprovado, sua média foi {pt}')
elif 5<pt<=6.9:
    print(f'Você está de recuperação, sua média foi {pt}')
elif pt>=7:
    print(f'Você está aprovado, sua média foi {pt}')