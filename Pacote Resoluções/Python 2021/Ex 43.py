weight=float(input('Qual o seu peso? '))
hight=float(input('Qual a sua altura?(cm) '))
h=hight/100
imc=(weight/(h**2))
if imc<18.5:
    print(f'Seu IMC é {imc}')
    print('Você está abaixo do peso')

elif 18.5 < imc <= 25:
    print(f'Seu IMC é {imc}')
    print('Seu peso é o idela para você')
elif 25 < imc <= 30:
    print(f'Seu IMC é {imc}')
    print('Você está no sobrepeso')
elif 30 < imc <= 40:
    print(f'Seu IMC é {imc}')
    print('Você está obeso')
else:
    print(f'Seu IMC é {imc}')
    print('Você está na obesidade morbida')