"""Realizar el algoritmo para obtener la suma de los números pares desde 2 hasta 1.000 inclusive. """

numero=2
cont=0
suma=0

while cont<1000:
    suma=suma+numero
    numero=numero+2
    cont=cont+1
print("El resultado de la suma de todo los numeros pares son: ",suma)
