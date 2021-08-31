import random
from time import sleep
jokenpon=str(input(' PEDRA PAPEL TESOURA: ').upper())
if jokenpon=="PEDRA" or jokenpon=="TESOURA" or jokenpon=="PAPEL":
    sof=['PEDRA','PAPEL','TESOURA']
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    rad=random.choice(sof)
    print(f'O computador jogou {rad}')
    if jokenpon=='PAPEL' and rad=='TESOURA':
        print('O computador ganhou')
    elif jokenpon=='TESOURA' and rad=='PEDRA':
        print('O computador ganhou')
    elif jokenpon=='PEDRA' and rad=='PAPEL':
        print('O computador ganhou')
    elif jokenpon==rad:
        print('Empatou')
    else:
        print('Parabéns...Você ganhou ')
else:
    print('Jogada invalida...')