"""2.Realice un algoritmo que lea caracteres mientras no se digite el caracter "!". Mostrar al final 
cúantas vocales se ingresaros.
cuántas "x" se ingresaron."""



Vocales=0
Nx=0
Caracter=str(input("Ingrese un caracter: "))
if Caracter=="a" or Caracter=="e" or Caracter=="i" or Caracter=="o" or Caracter=="u" :
        Vocales+=1
if Caracter=="x":
        Nx+=1
while Caracter!= "!" :
    Caracter=str(input("Ingrese otro caracter: "))
    if Caracter=="a" or Caracter=="e" or Caracter=="i" or Caracter=="o" or Caracter=="u" :
        Vocales+=1
    elif Caracter=="x":
        Nx+=1
print("Cantidad de veces ingresada la X:",Nx,"Cantidad de Vocales ingresadas: ",Vocales)