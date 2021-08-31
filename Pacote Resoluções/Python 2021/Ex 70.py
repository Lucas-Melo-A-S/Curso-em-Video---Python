c=0
a=0
m=0
while True:
    print('-='*20)
    print('{:^40}'.format('LOJA DO LUCAS'))
    print('-='*20)
    p=str(input('Digite o nome do produto: '))
    r=float(input('Qual o valor do produto R$'))
    c+=1
    a+=r
    if c==1:
        br=r
        b=p
    if r > 1000:
        m+=1
    if br>r:
        br=r
        b=p
    e=str(input("Você deseja continuar [S/N]").upper()[0])
    while e!='S' and e!= 'N':
        e = str(input("Você deseja continuar [S/N]").upper()[0])
    if e =='N':
        break
print(f'''O total gasto foi de R${a}
A quantidade de produtos acima de R$ 1000,00 foi de {m} produto
O produto mais barato foi {b} com o valor de {br} reais''')

