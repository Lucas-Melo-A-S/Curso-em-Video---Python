l1=float(input('Qual o comprimento desse lado1: '))
l2=float(input('Qual o comprimento desse lado2:'))
l3=float(input('Qual o comprimento desse lado3: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    if l1==l2==l3:
        print('O triangulo é equilatero')
    elif l1==l2 or l2==l3 or l3==l1:
        print('O triangulo é Isosceles')
    elif l1 != l2 != l3:
        print('O triangulo é escaleno')
else:
    print('Não é triangulo')