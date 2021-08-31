def notas(*nota,sit=False):
    """
    Função que deve calcular a notas e da a media, quantas notas foram,a maior e menor nota e tudo isso deverá ser
    inserida em uma biblioteca.
    :param nota: Inserir todas as notas do aluno
    :param sit: Colocar True ou False para saber como está a situação do aluno
    :return: Retorna uma biblioteca com todos os dados cadastrados pelo função

    MADE BY LUCAS MELO
    """
    soma_nota=len(nota)
    c = list(nota)
    c1 = c[0]
    c2 = c[0]
    cs=0
    x=0
    while x < soma_nota:
        if c1<c[x]:
            c1=c[1]
        if c2 >= c[x]:
            c2=c[x]
        x += 1
    for t in c:
        cs+=t
    media=(cs/soma_nota)
    biblioteca={'Total': soma_nota, 'Maior': c1, 'Menor':c2, 'Média':media }
    if sit == True:
        if media >= 7:
            sit = 'Aprovado'
            print('Aprovado')
        else:
            sit ='Você deve melhorar'
        biblioteca['situação'] = sit
    return(biblioteca)


print(notas(6.5,8.5,3,5.4,sit=True))
