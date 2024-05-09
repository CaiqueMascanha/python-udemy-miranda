nome = 'Caique'
interando = 0
novo_nome = ''

while interando < len(nome):
  letra = nome[interando]
  novo_nome += f'*{letra}'
  interando += 1
  
print({f'{novo_nome}*'})