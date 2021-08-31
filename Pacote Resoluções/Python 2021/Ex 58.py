from random import randint
pc=randint(0,10)
n=int(input('Digite um numero entre 0 e 10: '))
c=1
while pc != n:
    if n<pc:
        n = int(input('Mais..Digite um numero entre 0 e 10: '))
    elif n>pc:
        n = int(input('Menos..Digite um numero entre 0 e 10: '))
    c += 1
print(f'Parabéns você acertou, você precisou de {c}x para acertar')

