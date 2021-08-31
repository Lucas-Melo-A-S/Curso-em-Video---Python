dist=float(input('De quantos quilometros será sua viagem: '))
if dist<=200:
    print(F'O valor da sua passagem será R${0.5*dist} sendo 50 centavos por km ')
else:
    print(f'O valor da sua passsagem é R${0.45*dist}, sendo 45 centavos por km')