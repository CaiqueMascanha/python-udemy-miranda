# raise - lançando exceções (erros)
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float,'
                        f' você mandou: {tipo.__name__}')
    return True

def divide(n, d):
    nao_aceito_zero(d)
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    return n / d


print(divide(8,'0'))