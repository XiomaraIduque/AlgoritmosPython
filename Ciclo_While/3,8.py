"""una estación climática proporciona un par de temperaturas diarias 
(máxima, mínima) 
(no es posible que alguna o ambas temperaturas sea 9 grados). 
La pareja fin de temperaturas es 0,0. 
Se pide determinar el número de días, cuyas temperaturas se han proporcionado. 
Las medias máxima y mínima
El número de errores —temperaturas de 9°— y el porcentaje que representaban"""


Dias=0
Errores=0
Temp1=  float
Temp2=float
Suama=0
SMax=0
SMin=0
while Temp1!= 0 and Temp2!= 0 :
    Temp1=float(input("Ingrese la Maxima   temperatura : "))
    Temp2=float(input("Ingrese la Minima  temperatura : "))
    Suama= Suama+ 2 
    SMax= SMax + Temp1
    SMin= SMin + Temp2
    if  Temp1==9 :
        Errores= Errores+1
        Dias= Dias +1
    if Temp2==9:  
        Errores= Errores+1
        Dias= Dias +1  
    else:
         Dias= Dias +1
if Errores== 0 :
    Promedio= 0
else:
    Promedio=Suama/Errores
Porcen=(Errores*100)/Suama
PromeMax=SMax/Suama
PromeMin=SMin/Suama
print("-------------------------------------------------------------------------------------------")
print("Numero de dias ingresados:",Dias)
print("---------------------------------------")
print("El numero es de Errores es :", Errores)
print("---------------------------------------")
print("El Promedio es:",Promedio)
print("---------------------------------------")
print("Porcenntaje de Errores es: ",Porcen)
print("---------------------------------------")
print("Promedio Temp Max: ",PromeMax,"Promedio Temp Mini",PromeMin)
