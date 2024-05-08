# Este é um decorador que recebe uma função como argumento.
def criar_funcao(func):
    # A função interna é o decorador propriamente dito.
    def interna(*args, **kwargs):
        print('Vou te decorar')
        # Antes de chamar a função original, verifica se todos os argumentos são strings.
        for arg in args:
            e_string(arg)
        # Chama a função original com os argumentos fornecidos.
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        # Retorna o resultado da função original.
        return resultado
    # Retorna a função decorada.
    return interna

# Este decorador é aplicado à função invert_string.
@criar_funcao
def invert_string(string):
    # A função inverte a string fornecida.
    return string[::-1]

# Esta função auxiliar verifica se o argumento fornecido é uma string.
def e_string(string):
    if not isinstance(string, str):
        # Se não for uma string, levanta um erro.
        raise TypeError('Você deve informar uma String!')

# A função invert_string está comentada, mas pode ser usada para inverter strings.

# Este é um decorador com argumentos que retorna outro decorador.
def fabrica_de_decorarodes(a, b, c):
    # A função fabrica_de_funcoes é o decorador que será retornado.
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        # A função aninhada é o decorador propriamente dito.
        def aninhada(*args, **kwargs):
            print('Aninhada')
            # Chama a função original com os argumentos fornecidos.
            res = func(*args, **kwargs)
            # Retorna o resultado da função original.
            return res
        # Retorna a função decorada.
        return aninhada
    # Retorna o decorador.
    return fabrica_de_funcoes

# Este decorador é aplicado à função soma.
@fabrica_de_decorarodes(1, 2, 3)
def soma(x, y):
    # A função soma os dois argumentos fornecidos.
    return x + y

# Chama a função soma decorada e imprime o resultado.
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
