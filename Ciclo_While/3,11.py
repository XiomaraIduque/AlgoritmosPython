"""Leer las notas de una clase de algoritmos y 
deducir todas aquellas que son NOTABLES (> 4,5y <=5.0)"""



Numerodenotas=int(input("Ingrese la cantidad de notas: "))
Contador=0
s=0
b=0


while Contador<=Numerodenotas :
    notables=float(input("ingrese la nota: "))
    if  notables>4.5 and  notables <=5.0:
        s=s+1
        Contador=Contador+1  
        
    else: 
        b=b+1
        Contador=Contador+1

    
print("La cantidad de notas notables fueron: ",s)
print("La canitdad de vagos son: ",b)