valores = {
    'nome': 'Caique',
    'idade': 22,
    'profissão': 'Engenheiro de dados'
}




for chave, valor in valores.items():
    if isinstance(valor, int):
        print(f'É inteiro: {valor}')
    else:
        print(f'Não é inteiro: {valor}')