# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Solicitacao:
    def __init__(self, pedido):
        self.pedido = pedido

class Contrato(Solicitacao):
    def __init__(self, pedido, contrato):
        super().__init__(pedido)
        self.contrato = contrato

p = Solicitacao(123)
# print(p.pedido)

c = Contrato(p.pedido, 789)
print(c.pedido)
print(c.contrato)