""" realice un algoritmo que lea N numeros enteros y calcular y mostrar 
cuantos positivos y cuantos negativos"""

N=0
NumerosPositivos=0
NumerosNegativos=0
contador=0
l=0

N=int(input("ingrese la cantidad de numeros:  "))

for X in range (1,N+1):
    numero = int(input("ingrese numero"))

    if numero>0:
        NumerosPositivos=NumerosPositivos+1
        
    elif numero==0:
       l=l+1
    
    else:
        NumerosNegativos=NumerosNegativos+1
       


print("Los numeros negativos son: ",NumerosNegativos)
print("Los numeros positivos son: ",NumerosPositivos)
print("Los numeros en 0 son: ",l)
