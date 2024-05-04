"""Calcular la suma de los n primeros números enteros utilizando la estructura para."""

x=0 #ES UN ACOMULADOR
m=int(input("Digite la cantidad de numeros a ingresar: "))
for f in range (1, m+1):
    w=int(input("Escriba un numero: "))
    x=x+w
print("Este es el resultado de la suma: ",x)