"""7.Realice un algoritmo que lea números enteros mientras no se digite el -99
Calcular y mostrar:
Cantidad de positivos
Cantidad de negativos
Cantidad de pares
Cantidad de impares
Cantidad de pares positivos
Cantidad de pares negativos
Suma de pares positivos
Suma de impares positivos
Suma de unos ingresados."""



Numero=0
CP=0
CN=0
CPA=0
CMPA=0
CPP=0
CMPAN=0
CPAN=0
CIMPAP=0
Numer1=0
Parespositivos=[]
Imparesnegativo=[]
while Numero!= -99:
    Numero=int(input("Ingrese un numero: "))
    if Numero>0 :
        CP+=1
    if Numero%2==0 :
        CPA+=1
    if Numero>0 and Numero%2==0 :
        CPP+=1
        Parespositivos.append(Numero)
    if Numero<0:
        CN+=1
    if Numero%2>0 and Numero>0 and Numero!=-99:
        CMPA+=1
        Imparesnegativo.append(Numero)
    if Numero<0 and Numero%2>0 and Numero!=-99 :
        CMPAN+=1
    if Numero<0 and Numero%2==0 :
        CPAN+=1
    if Numero==1:
        Numer1+=1
print("\n")
print("Cantidad de Numeros Positivos Ingresados: ",CP)
print("Cantidad de Numeros Negativos Ingresados: ",CN)
print("Cantidad de Numeros Pares Ingresados : ",CPA)
print("Cantidad de Numeros Impares Ingresados: ",CMPA)
print("Cantidad de Numeros Pares Positivos: ",CPP)
print("Cantidad de Numeros Impares Positivos Ingresados: ",CMPA)
print("Cantidad de Numeros Pares Negativos:",CPAN)
print("Cantidad de Numeros Impares Negativos:",CMPAN)

print("La suma de los pares positivos es:",sum(Parespositivos))
print("La suma de los impares positivos es: ",sum(Imparesnegativo))
print("La suma de los 1 ingresados es: ",Numer1)
