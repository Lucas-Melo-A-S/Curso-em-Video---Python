import random
a1=str(input('Qual o nome do aluno1: '))
a2=str(input('Qual o nome do aluno2: '))
a3=str(input('Qual o nome do aluno3: '))
a4=str(input('Qual o nome do aluno4: '))
r=random.choice([a1,a2,a3,a4])
print(f'Os alunos escolhidos fora {a1}, {a2}, {a3}, {a4} e o escolhido foi...')
print(r)