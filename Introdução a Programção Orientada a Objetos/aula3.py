import json

CAMINHO_ARQUIVO = 'aula.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Caique', 22)
p2 = Pessoa('Jeniffer', 22)
p3 = Pessoa('Lohane', 22)

bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='UTF-8') as arquivo:
    json.dump(bd, 
              arquivo,
              indent=2,
              ensure_ascii=False)