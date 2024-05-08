import time
from datetime import datetime
import os
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR')

i = 1

while True:
    os.system('cls')
    data_atual = datetime.now().strftime('%d de %B de %Y').capitalize()
    hora_Atual = datetime.now().strftime('%H:%M:%S')
    print(data_atual)
    print(hora_Atual)
    time.sleep(1)
    print(i)
    i += 1