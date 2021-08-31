r1=float(input('Digite uma reta: '))
r2=float(input('Digite uma reta: '))
r3=float(input('Digite uma reta: '))
if r1>r2 and r1>r3:
    if r1<r2+r3:
        print('Com as retas pode formar um triangulo')
    if r1>=r2+r3:
        print('Não pode fazer um triangulo')
if r2>r1 and r2>r3:
    if r2<r1+r3:
        print('Com as retas pode formar um triangulo')
    if r2>=r1+r3:
        print('Não pode fazer um triangulo')
if r3>r1 and r3>r2:
    if r3<r1+r2:
        print('Com as retas pode formar um triangulo')
    if r3>=r1+r2:
        print('Não pode fazer um triangulo')

#Simplificação
r1=float(input('Digite uma reta: '))
r2=float(input('Digite uma reta: '))
r3=float(input('Digite uma reta: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Com as retas pode formar um triangulo')
else:
    print('Não pode fazer um triangulo')