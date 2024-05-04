"""Determinar los valores máximo y mínimo de una lista de 10 números ingresados por teclado"""

mayor=-9999999999999999999999999999999999999999999999999999999
menor=99999999999999999999999999999999999999999999999999999999

for e in range (1, 11):
    s=int(input("Ingrese numero: "))
    if mayor<s:
        mayor=s
    elif menor>s:
        menor=s
print("El numero mayor es: ",mayor )
print("EL numero menor es: ",menor )