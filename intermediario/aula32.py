numero = input('Digite um número inteiro: ')

try:
  numero_int = int(numero)
  if numero_int % 2 == 0:
    print(f'O número {numero_int} é par')
  else:
    print(f'O número {numero_int} é ímpar')
except:
  print('Você não digitiu um número inteiro')
  

manha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tarde = [12, 13, 14, 15, 16, 17]
noite = [18, 19, 20, 21, 22, 23]

hora = input('Qual horário? ')

try:
  hora = int(hora)
  if hora in manha:
    print('Bom dia')
  elif hora in tarde:
    print('Boa tarde')
  else:
    print('Boa noite')
except:
  print('Digite um horário válido')
  
nome = input('Digite seu nome: ')

if len(nome) <= 4:
  print('Seu nome é curto')
elif len(nome) > 4 and len(nome) <= 6:
  print('Seu nome é normal')
else:
  print('Seu nome é muito grande') 
