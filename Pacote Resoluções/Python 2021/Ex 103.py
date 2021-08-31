def ficha(nome, gols,ass):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    if ass == '':
        ass = 0
    return (f'''O jogador {nome}, fez {gols} gol(s) e deu {ass} assistencias no campeonato''')


n=str(input('Qual o nome do jogador: ').upper())
g=(input('Quantos gols ele fez: '))
a=(input('Quantas assistencias ele fez: '))
print(ficha(n,g,a))
