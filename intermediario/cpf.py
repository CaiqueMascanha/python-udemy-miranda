# Solicite ao usuário que insira o CPF
cpf = input("Digite o CPF (apenas números): ")

# Verifique se o CPF tem 11 dígitos (tamanho padrão de um CPF)
if len(cpf) == 11:
    # Inicialize uma variável para armazenar o CPF formatado
    cpf_formatado = ""

    # Use um loop for para formatar o CPF
    for i in range(14):
        # Adicione um ponto após cada bloco de 3 dígitos
        if i in (2, 5):
            cpf_formatado += "."
        # Adicione um hífen após o sexto bloco de 3 dígitos
        elif i == 8:
          cpf_formatado +='/'
        elif i == 12:
            cpf_formatado += "-"
        
        # Adicione o dígito atual à string formatada
        cpf_formatado += cpf[i]

    # Exiba o CPF formatado
    print("CPF formatado:", cpf_formatado)
else:
    print("O CPF deve conter exatamente 11 dígitos.")