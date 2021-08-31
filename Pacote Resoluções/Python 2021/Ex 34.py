salary=float(input('Qual o seu salario?: '))
if salary>1250:
    print('Seu salario é superior a R$1200,00, seu aumento será de 10%')
    print(f'O seu novo salario será R${salary*1.1}')
else:
    print('Seu salario é inferior a R$1200,00, seu aumento será de 15%')
    print(f'Seu novo salario será R${salary*1.15}')