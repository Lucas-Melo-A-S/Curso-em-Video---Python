num=int(input('Digite um numero: '))
choose=int(input('''Escolha as opções:
1 - Numeros Binarios
2 - Numeros Octal
3 - Numeros Hexadecimal
: '''))
if choose == 1:
    print(f'Você escolheu a opção BINARIA, sue numero nessa opção é {bin(num)}')
elif choose == 2:
    print(f'Você escolheu a opção OCTAL, sue numero nessa opção é {oct(num)}')
elif choose == 3:
    print(f'Você escolheu a opção HEXADECIMAL, sue numero nessa opção é {hex(num)[2:]}')
else:
    print('Numero invalido')
