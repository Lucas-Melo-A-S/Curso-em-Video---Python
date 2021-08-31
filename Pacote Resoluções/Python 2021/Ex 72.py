numbers=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Ste','Oito','Nove','Dez','Onze','Doze','Treze','Quartorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
t=int(input('Digite um numero entre 0 e 20 : '))
while True:
    if t < 0 or t > 20:
        t=int(input('Numero errado, digite entre 0 e 20: '))
    else:
        break
print(f'O numero digitado foi {numbers[t]}')
