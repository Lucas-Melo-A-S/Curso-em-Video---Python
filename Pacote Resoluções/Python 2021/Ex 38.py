num1=float(input('Digite um numero: '))
num2=float(input('Digite um numero: '))
if num1>num2:
    print(f'O primeiro valor {num1} é maior que o segundo valor {num2}')
elif num2>num1:
    print(f'O segundo valor {num2} é maior que o primeiro {num1}')
elif num1==num2:
    print('Os numeros são iguais')