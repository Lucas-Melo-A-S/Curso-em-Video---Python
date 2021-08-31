s = str(input('Digite o seu sexo [M/F]: ').upper())[0]
while s not in 'M' and 'F':
    s=str(input('Sexo invalido...Por favor digite um valido: ').upper())[0]
print(f'Sexo adicionado com sucesso')