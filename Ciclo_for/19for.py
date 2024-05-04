"""Generar las horas, minutos y segundos de 1 dia terrestre con formato de 24 horas. Ejemplo:

0:0:0
0:0:1
0:0:2
……..
11:11:11
…….
23:59:58
23:59:59"""

for horas in range (25):
    for minutos in range(60):
        for segundos in range (60):
            print(horas, minutos, segundos)
