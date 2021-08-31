house=float(input('Qual o valor da casa? R$ '))
salary=float(input('Qual o seu salario? R$ '))
year=int(input('Em quantos anos você pretende comprar sua casa? '))
month=year*12
ps=house/month
if salary * 0.3 >= (ps):
    print(f'Parabéns seu emprestimo foi aceito, o valor pago será de R${ps} ')
else:
    print(f'Emprestimo Negado, sua prestação seria de R${ps} e 30% do seu salario R$   {salary*0.3} não será o suficiente')