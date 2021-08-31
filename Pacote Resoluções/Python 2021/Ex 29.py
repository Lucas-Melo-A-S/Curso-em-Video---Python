speed=float(input('Digite a velocidade que o carro passou na avenida: '))
if speed >80:
    print(f'Você ultrapassou a velocidade maxima de 80 km, sua velocidade era {speed}km/h')
    print(f'Você receberá uma multa de {(speed-80)*7} reais por ter ultrapassado a velocidade maxima em {speed-80} km/h')
else:
    print('No limite da via')