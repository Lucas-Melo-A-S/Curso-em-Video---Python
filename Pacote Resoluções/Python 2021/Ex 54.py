from datetime import datetime
diaatual=datetime.today().year
menor=0
maior=0
for c in range(1,8):
    a=int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    if (diaatual-a)<18:
        menor+=1
    elif (diaatual-a)>=18:
        maior+=1
print(f'No questionario feito foram encontrados {menor} menor de idade e {maior} maior de idade')