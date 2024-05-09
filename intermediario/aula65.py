def saudacao(nome):
    try:
        print(f'Olá {nome}!')
    except SyntaxError:
        print('Você deve fornecer seu nome!')
    except TypeError:
        print('Você deve fornecer seu nome!')

saudacao()