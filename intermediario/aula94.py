def adicionar_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adicionar_clientes('Caique')
adicionar_clientes('Jeniffer', cliente1)
print(cliente1)