nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
  print(f'Seu nome é: {nome}')
  print(f'Seu nome invertido é: {nome[::-1]}')
  if ' ' in nome:
    print('Seu nome tem espaços')
  else:
    print('Seu nome não tem espaços')
    print(f'seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome é {nome[0]}')
  print(f'A primeira letra é {nome[-1]}')
else:
  print('Você não preencheu todos os campos')