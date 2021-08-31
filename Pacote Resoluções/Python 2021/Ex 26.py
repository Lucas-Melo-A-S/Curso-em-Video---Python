phrase=str(input('Digite uma frase: ').upper().strip())
print(f'Na sua frase a letra A"aparece {phrase.count("A")} vezes')
print(f'A posição do primeiro "A" é {phrase.find("A")+1}' )
print(f'A posição do ultimo "A" é {phrase.rfind("A")+1}')