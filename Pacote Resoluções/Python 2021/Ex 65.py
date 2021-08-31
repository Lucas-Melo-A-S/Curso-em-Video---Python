z=0
s=0
while True:
    x=int(input('Digite um numero: '))
    z+=1
    s+=x
    if z==1:
        min=x
        m=x
    if m<x:
        m=x
    if min>x:
        min=x
    c= str(input('Você deseja continuar: ').upper())
    if c =='N':
        break
print(f'''A média dos numeros foi {s/z}
O maior numero é {m}
O menor numero é {min}''')