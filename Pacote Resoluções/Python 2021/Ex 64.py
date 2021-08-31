x=0
y=0
while True:
    z=int(input('Digite um numero: [Para parar digite 999: '))
    if z!= 999:
        x+=1
        y+=z
    else:
        break
print(f'A quantidade de numeros digitados foi {x} e a soma entre eles é {y}')

