"""10. Calcular el enésimo término de la serie de Fibonacci definida por:
A1 = 1   A2 = 2   A3 = 1 + 2 =3
A4=5  A5=8

An = An - 1 + An -  2 (n >= 3) """

aux=0
n=0
inicio=0
siguiente=0

n= int(input("Ingrese el numero hasta donde va la serie de FIBONACCI: "))

for i in range (1,n+1,1):
    r=inicio +siguiente
    aux=r
    r=inicio
    inicio=siguiente
    siguiente=aux
print(r,end=",")