palavra=input('Digite a palavra secreta: ').lower().strip()
for x in range(100):
    print()
digitados=[]
acertos=[]
erros=0
while True:
    senha=''
    for letra in palavra:
        if letra in acertos:
            senha+=letra
        else:


































































            senha+='.'
        print(senha)
    if senha == palavra:
        print("VocÊ acertou")
        break
    tentativa=input('\nDigite uma letra').lower().strip()
    if tentativa in digitados:
        print('Você já tentou essa letra')
        continue
    else:
        digitados+=tentativa
        if tentativa in palavra:
            acertos+=tentativa
        else:
            erros+=1
            print('Você errou')
