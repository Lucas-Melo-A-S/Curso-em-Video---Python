import datetime
year=int(input('Digite um ano, digite 0 para sinalizar o ano atual: '))
if year==0:
    year=datetime.date.today().year
if year%4==0 and year%100!=0 or year%400==0:
    print(f'O ano {year} é BISSEXTO')
else:
    print(f'O ano {year} não é BISSEXTO')