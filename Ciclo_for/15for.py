"""Realizar un algoritmo que lea un número entero positivo
y determine si es perfecto o no."""

suma=0
numero=int(input("Digite un numero: "))

for i in range (1,numero):
    if numero%i==0:
        suma=suma+i
if suma==numero:
    print("Si Es Un Número Perfecto",suma)
else:
    print("NO Es Un Número Perfecto",)