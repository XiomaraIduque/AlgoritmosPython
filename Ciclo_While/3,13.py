
"""Generar los primeros 99 múltiplos positvos del 3 empezando en 3"""

numero=3

while numero<99:
    numero=numero+1
    if numero%3==0:
        print("Estos son los multiplos del 3 hasta el 99: ",numero)
        numero=numero+1
    else: 
        numero+1


