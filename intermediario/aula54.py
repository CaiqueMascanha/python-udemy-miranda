
import os 

lista = []

while True:
    print('Selecione uma opção:')
    valor_usuario = input('[i]nserir [a]pagar [l]istar: ').lower()
    if valor_usuario == 'i':
        os.system('cls')
        valor = input('Digite o valor para inserir: ')
        if valor in lista:
            print('Este valor já está em sua lista!')
        lista.append(valor)
    elif valor_usuario == 'a':
        try:
            indece = int(input('Digite o indice para apagar: ')) - 1
            del lista[indece]
        except ValueError:
            print('Digite um número inteiro do índice!')
        except IndexError:
            print('Digite um índice inteiro da lista!')
    elif valor_usuario == 'l':
        os.system('cls')
        print('### Listando Valores ###')
        for i, valor in enumerate(lista, 1):
            print(i, valor)
    else:
        print('Escolha uma opção válida!')