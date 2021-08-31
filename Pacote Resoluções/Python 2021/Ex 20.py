import random

a1=str(input('Qual o nome do aluno1: '))
a2=str(input('Qual o nome do aluno2: '))
a3=str(input('Qual o nome do aluno3: '))
a4=str(input('Qual o nome do aluno4: '))
r=[a1,a2,a3,a4]
random.shuffle(r)
print(f'Os alunos escolhidos fora {a1}, {a2}, {a3}, {a4} e a lista de apresentação será ...')
print(r)