def voto(y):
    from datetime import datetime
    n=datetime.today().year
    if (n-y) > 18 and ((n-y) < 65):
        print(f'Você tem {n-y}, seu voto é obrigado')
    elif 18>(n-y)>16 or ((n-y) >= 65):
        print(f'Você tem {n-y}, Seu voto é opcional')
    else:
        print(f'Você tem {n-y}, não pode votar')

print('-='*15)
a=int(input('Em que ano você nasceu: '))
voto(a)