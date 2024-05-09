numero = range(10)
numeros = range(5, 10)
numero = 1578965
numeros = range(0,numero * 10 + 1,numero)
inicial = 0
for i in numeros:
  print(f'{numero} x {inicial} = {i}')
  inicial += 1