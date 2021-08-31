import datetime
y=datetime.date.today().year
by=int(input('Você nasceu em qual ano ? '))
d=y-by
if d<18:
    print(f'Você ainda vai se alistar, ainda faltam {18-d}')
elif d==18:
    print(f'Você deve se alistar de imediato')
elif d > 18:
    print(f'Você deve se alistar com urgência, já se passaram {d-18}')
