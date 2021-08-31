soma=0
for i in range (1,500):
    if i%2!=0 and i%3==0:
      soma+=i
      print(f'A soma até o momento está dando {soma}')
print(soma)

