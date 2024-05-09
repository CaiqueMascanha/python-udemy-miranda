def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total

def par_ou_impar(*args):
    resultado = {'pares': [], 'impares': []}
    for num in args:
        if num % 2 == 0:
            resultado['pares'].append(num)
        else:
            resultado['impares'].append(num)
    return resultado

# print(1*2*3)
# numeros = 1,2,3
# result = mult(*numeros)
# result2 = mult(1,2,3)
# print(result)
# print(result2)
            
value = par_ou_impar(1,2,3,4,5,6,7,8,9)
print(value)