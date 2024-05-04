"""Dado un entero positivo n (> 1), comprobar si es primo o no."""

contador=0
numero=int(input("Digite un numero entero mayor a 1: "))

for i in range (1,numero+1):
    if numero%i==0:
        contador=contador+1
if contador>2:
        print("Este número no es primo",numero)
else:
        print("Si es un número primo",numero)