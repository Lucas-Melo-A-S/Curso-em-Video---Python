import datetime
y=datetime.date.today().year
ay=int(input('Qual ano seu filho nasceu? '))
m=y-ay
if m <= 9:
    print(f'Seu filho tem {m} anos e ele é da categoria MIRIM')
elif 9 < m <= 14:
    print(f'Seu filho tem {m} anos e ele é da categoria INFANTIL')
elif 14 < m <= 19:
    print(f'Seu filho tem {m} anos e ele é da categoria INFANTO')
elif 19 < m <=20:
    print(f'Seu filho tem {m} anos e ele é da categoria JUVENIL')
else:
    print(f'Seu filho tem {m} anos e ele é da categoria MASTER')