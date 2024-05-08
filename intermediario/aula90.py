iterable = ['Eu', 'Tenho', '__inter__']
iterator = iter(iterable)

# Generator faz desta forma, como se fosse tupla e não salva na memoria, poupando espaço
generator = (n for n in range(10))
print(iterator)