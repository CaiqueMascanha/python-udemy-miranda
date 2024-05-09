salas = [

    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'joão', 'Eduarda', (0, 1, 2, 3, 4)]

]

print(salas[2][3][2])

for sala in salas:
    print(f'A sala é: {sala}')
    for aluno in sala:
        print(aluno)
        #for numeros in aluno:
        #    print(numeros)
