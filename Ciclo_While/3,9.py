
#. Leer N números y mostrar:
#cuántos son múltiplos del 2 y 3 y 4
#cuántos son múltiplos del 2 ó 9.

N=int(input("Digite la cantidad de Numeros que desea ingresar : "))
Contador=0
while N!=Contador :
    Numero=int(input("Ingrese un numero: "))
    Contador+=1
    if Numero%2==0 and Numero%3==0 and Numero%4==0 :
        print("El numero es Multiplo de 2 y 3 y 4 ")
    if Numero%2==0 or Numero%9==0 :
        print("El numero es Multiplo de 2 ó de 9 ")