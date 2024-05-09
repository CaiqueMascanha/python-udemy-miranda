import re
import sys
import random

print(random.randint(0,9))




regressiva_1 = 10
regressiva_2 = 11
index_max_cpf = 8

cpf_usuario = input('Informe seu CPF: ')
cpf_usuario = re.sub(r'[^0-9]', '', cpf_usuario)
cpf_validar_1 = cpf_usuario[:9]

mult_1 = 0
mult_2 = 0

for numero in cpf_validar_1:
    mult_1 += int(numero) * regressiva_1
    print(f'Valor a multiplica: {int(numero)} X {regressiva_1} = {mult_1}')
    regressiva_1 -= 1

resultado_primeiro_digito = (mult_1 * 10) % 11

cpf_validar_2 = cpf_validar_1 + str(resultado_primeiro_digito)
print(cpf_validar_2)

for numero in cpf_validar_2:
    mult_2 += int(numero) * regressiva_2
    #print(f'Valor a multiplica: {int(numero)} X {regressiva_2} = {mult_2}')
    regressiva_2 -= 1

resultado_segundo_digito = (mult_2 * 10) % 11

if resultado_primeiro_digito <= 9:
    resultado_primeiro_digito = resultado_primeiro_digito
else:
    resultado_primeiro_digito = 0

if resultado_segundo_digito <= 9:
    resultado_segundo_digito = resultado_segundo_digito
else:
    resultado_segundo_digito = 0

print(resultado_primeiro_digito, resultado_segundo_digito)