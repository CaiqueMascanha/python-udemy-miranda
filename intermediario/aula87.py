lista = [True, 1, 2, 10, 5.8, 5.879645, 'Caique', 'j']

for i in lista:
    print(i, isinstance(i, str))

valor = input('Digite um valor: ')
print(valor.isdecimal())
if valor.isidentifier():
    
    print('Você digitou um número!')
else:
    print('Você não digitou um número!')