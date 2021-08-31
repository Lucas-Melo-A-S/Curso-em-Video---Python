w=str(input('Digite uma frase: ').strip().upper())
w1=w.split()
w2=''.join(w1)
i=''
for c in range(len(w2)-1,-1,-1):
    i+=w2[c]
print(i)
print(w2)
if w2==i:
    print('É um palindromo')
else:
    print('Não é um palindromo')
