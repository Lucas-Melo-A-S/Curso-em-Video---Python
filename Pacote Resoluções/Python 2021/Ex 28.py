import random
import time
number=random.randint(0,5)
choice=int(input('Escolha um numero entre 0 e 5: '))
print('Estou pensando em um numero')
time.sleep(2)
if choice == number:
    print(f'Parábens você escolheu o mesmo numero do computador')
else:
    print(f'Tente mais uma vez, o computador escolheu o numero {number} e você escolheu {choice}')