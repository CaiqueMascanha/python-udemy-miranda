class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    def inserir_motor(self, nome):
        self.motor.append(Motor(nome))

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

punto = Carro('Punto')
fiat = Fabricante('Fiat')
etorq_1_6 = Motor('Etorq 1.6')
punto.fabricante = fiat
punto.motor = etorq_1_6
print(punto.nome, punto.fabricante.nome, punto.motor.nome)