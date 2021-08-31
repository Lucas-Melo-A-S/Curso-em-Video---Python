from random import randint
co=str(input('PAR OU IMPAR: ').upper())
n=int(input('Escolha seu numero: '))
r=randint(0,100)
f=(n+r)
print(r)
c=0
while True:
    if co=='PAR' and (f)%2==0:
        print(f'Parabéns você ganhou, {f} é par')
        c += 1
        co = str(input('PAR OU IMPAR: ').upper())
        n = int(input('Escolha seu numero'))
        break
    elif co=='IMPAR' and f%2!=0:
        print(f'Parabéns você ganhou, {f} é impar')
        c += 1
        co = str(input('PAR OU IMPAR: ').upper())
        n = int(input('Escolha seu numero'))
        break
    elif co =='PAR' and f%2!=0:
        print('A maquina ganhou, GAME OVER')
        break
    elif co =='IMPAR'and f%2==0:
        print('A maquina ganhou, GAME OVER')
        break
print(f'Você ganhou {c}x da maquina')