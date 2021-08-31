d=0
n=0
a=0
m2=0
for c in range(1,5):
    print('-'*10,c,'ª PESSOA','-'*10)
    name=str(input('Qual o seu nome:'))
    age=int(input('Qual a sua idade:'))
    gender=str(input('Qual o seu sexo: [F/M]').upper())
    a+=age
    d+=1
    if gender=="F" and age < 20:
        m2+=1
    elif gender=="M":
        if n<=age:
            n1=name
            n=age
m=a/d
print(f'''A média de idade entre todos foi de {m}
Foi constatado que {m2} mulheres tem menos de 20 anos
O homem mais velho encontrado foi o {n1}''')
