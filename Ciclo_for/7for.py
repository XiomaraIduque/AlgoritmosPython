"""Se ingresan N números por teclado, calcular y mostrar el valor del número mayor."""

mayor = -99999999999
contador = 0
N = int(input("Digite cantidad de números:"))
numeroIngresado = 0
for contador in range(1,N+1):
    numeroIngresado = int(input("digite un numero: "))
    if mayor < numeroIngresado:
        mayor = numeroIngresado

print("El número mayor es: ",mayor)
