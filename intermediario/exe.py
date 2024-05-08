import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos2 = copy.deepcopy(produtos)

for i in produtos2:
    i['preco'] = round(i['preco'] * 1.10, 2)

produtos2 = sorted(produtos2, key=lambda p: p['nome'], reverse=True)
    
print(*produtos, sep='\n')
print()
print(*produtos2, sep='\n')
