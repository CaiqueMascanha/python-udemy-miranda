# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
print(duplicar(5))