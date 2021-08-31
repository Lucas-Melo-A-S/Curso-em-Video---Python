i18=0
m=0
f20=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    n=str(input('Qusl o seu nome: '))
    i=int(input('Qual a sua idade: '))
    s=str(input('Qual o seu sexo: [M/F]').upper()[0])
    while s!='M' and s!='F':
        s = str(input('Qual o seu sexo: [M/F]').upper()[0])
    if i>18:
        i18+=1
    if s=='M':
        m+=1
    if s =='F' and i < 20:
        f20+=1
    c=str(input('Você deseja continuar? [S/N]').upper()[0])
    while c!='S' and c!='N':
        c = str(input('Você deseja continuar? [S/N]').upper()[0])
    if c=='N':
        break

print(f'''Foram cadatrados {i18} pessoas acima de 18 anos;
foram cadatrados {m} homens;
Foram cadastrados {f20} mulheres abaixo dos 20 anos''')