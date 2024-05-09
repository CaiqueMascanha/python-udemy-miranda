# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    c = a/b
except ZeroDivisionError:
    print('Erro! Tentou dividir por zero!')
except NameError as e:
    print(f'Variavel {e}')