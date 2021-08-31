#list=[]
#for c in range(1,6):
   # t=int(input(f'Qual o peso da {c}ª pessoa: '))
    #p=list.append(t)
#print(f'O maior peso é {max(list)} e o menor numero é {min(list)}')

maior=0
menor=0
for c in range(1,6):
    t=float(input(f'Qual o peso da {c}ª pessoa: '))
    if c == 1 :
        maior= t
        menor = t
    else:
        if maior<=t:
            maior=t
        if t < menor:
            menor=t
print(f'O maior peso é {maior} e o menor numero é {menor}')