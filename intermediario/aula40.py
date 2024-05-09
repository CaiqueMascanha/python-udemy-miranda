""" Calculadora com while """

while True:
  sair = input('Quer sair? [s]im: ').lower().startswith('s')
  if sair:
    break
  num1 = input('Informe o primeiro número: ')
  num2 = input('informe o segunda número: ')
  operador = input("""Informe um dos operadores listados: 
+;
-;
/;
*;
  """)
  numeros_validos = None
  operadores_validos = '+-/*'
  
  try:
    num1 = float(num1)
    num2 = float(num2)
    numeros_validos = True
    if operador == '+':
      print(f'o resultado da soma é: {num1 + num2}')
    elif operador == '-':
      print(f'o resultado da subtação é: {num1 - num2}')
    elif operador == '*':
      print(f'o resultado da multiplicação é: {num1 * num2}')
    elif operador == '/':
      print(f'o resultado da divisão é: {num1 // num2}')
  except:
    numeros_validos = None
    
    if numeros_validos is None:
      print('Você não digitou um número válido')
      continue
    
  if operador not in operadores_validos:
    print('Você digitou um operador inválido')
    continue
  
  if len(operador) > 1:
    print('Digite apenas um operador')
    continue

