# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
finally:
    # Sempre será executado, independente se der errado ou não!
    print('FECHAR ARQUIVO')
