c=0
a=0
while True:
    n=int(input('Digite um numero: (Para para digite 999) '))
    if n!=999:
        a+=n
        c+=1
    else:
        break
print(f'A uqantidade de numero selecionados foi {c} e a soma deles é {a} ')