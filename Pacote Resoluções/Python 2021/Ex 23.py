number=str(input('Digite um numero entre 0 - 9999: '))
numbermais='000' + number
print(f'O seu numero é {number}')
print(f' unidade: {numbermais[-1]}')
print(f'dezena: {numbermais[-2]}')
print(f'Centena: {numbermais[-3]}')
print(f'Milhares: {numbermais[-4]}')

#numero=int(input('digite um numero: '))
#u= numero//1%10
#d=numero//10%10
#c=numero//100%10
#m=numero//1000%10
#print(f'O seu numero é {numero}')
#print(f'Unidade: {u}')
#print(f'Dezena: {d}')
#print(f'Centena: {c}')
#print(f'Milhares: {m}')