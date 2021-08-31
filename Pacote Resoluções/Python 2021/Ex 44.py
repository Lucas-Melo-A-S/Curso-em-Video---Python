payment=float(input('Digite o valor do produto: '))
tip=int(input('''Escolha a opção de pagamento:
1 - Á vista Dinheiro
2 - Á vista Cartão
3 - Cartão em até 2x (s/juros
4 - Cartão em até 3x (c/ 20% de juros)
:'''))
if tip == 1:
    print(f'Você terá um desconto de 10%, logo o seu pagamento será R${payment-(payment*0.1)}')
elif tip == 2:
    print(f'Você terá um desconto de 5%, logo o seu pagamento será R${payment-(payment*0.05)}')
elif tip == 3:
    print(f'O seu pagamento será R${payment} e poderá dividir em até 2x no valor de R${(payment/2)}')
elif tip == 4:
    n=int(input('Quantas parcelar você gostaria de ter?'))
    print(f'''Você poderá dividir em {n}x com uma multa de 20% de juros
a sua parcela final será de  {(payment*1.2)/n} em {n}x, sendo o valor final de {payment*1.2}''')
else:
    print('OPÇÃO INVALIDA')
