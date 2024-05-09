import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# # Abre (ou cria se não existir) um arquivo chamado 'aula.json' no modo de escrita.
# with open('aula.json', 'w', encoding='UTF-8') as arquivo:
#     # Usa a função dump do módulo json para escrever os dados do dicionário 'pessoa' no arquivo.
#     # O parâmetro 'ensure_ascii=False' permite caracteres unicode (como acentos) serem escritos corretamente.
#     # O parâmetro 'indent=2' formata o JSON para ser mais legível, adicionando 2 espaços para cada nível de indentação.
#     json.dump(pessoa, 
#               arquivo, 
#               ensure_ascii=False,
#               indent=2)

with open('aula.json', 'r', encoding='UTF-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)