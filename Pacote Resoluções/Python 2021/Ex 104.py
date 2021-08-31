def leiaint(b):
    while True:
        n = input(b)
        if n.isnumeric() == False:
            print('Erro´,Digite um numero inteiro: ')

        else:
            print(f'Você acabou de adicionar o numero {n}')
            return(n)
            break
leiaint('Digite um numero inteiro: ')






