perguntas = [
    {
        'Perguntas': 'Quanto é 2 + 2? ',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '4',
    },
    {
        'Perguntas': 'Quanto é 5 * 5? ',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Perguntas': 'Quanto é 10/2? ',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    },
]

def perguntar():
    ini = 0
    for i in perguntas:
        vl = perguntas[ini].values()
        print('\n' + list(vl)[0] + '\n')
        print('Opções:')

        for i in list(vl)[1]:
            print(i)
        # print(*opcoes, sep=', ')
        resposta = input('Digite sua resposta: ')
        if resposta == list(vl)[2]:
            print('Parabéns, você acertou! 😎')
            ini += 1
        else:
            print('Que pena, você errou! 😫')
        
        print('Parabéns, você acertou')
        
    

perguntar()