"""Leer 100 números. Determinar la media de los números
positivos y la media de los números negativos."""

contadorpositivo=0
contadornegativo=0
sumadepositivos=0
sumadenegativos=0
#promedionegativo=sumadenegativos/contadornegativo
#promediopositivo=sumadepositivos/contadorpositivo

for a in range (1,101):
    x=int(input("Ingrese un numero: "))
    if x>=1:
        contadorpositivo=contadorpositivo+1
        sumadepositivos=sumadepositivos+x
    else:
        contadornegativo=contadornegativo+1
        sumadenegativos=sumadenegativos+x

if contadorpositivo==0:
    contadorpositivo=1

if  contadornegativo==0:
    contadornegativo=1

print("Este es el promedio de los numeros positivos:",sumadepositivos/contadorpositivo)
print("Este es el promedio de los numeros negativos: ",sumadenegativos/contadornegativo)