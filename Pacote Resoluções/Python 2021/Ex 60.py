from math import factorial
x=int(input('Digite um valor para fatoriar: '))
a=1
d=factorial(x)
while x > 0:
    a *= x
    print(f'{x}', end='')
    print('x' if x> 1 else '=', end='' )
    x-=1
print(a)