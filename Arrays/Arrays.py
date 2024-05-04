

def eje2():

  # Crear un array A con 10 nombres de productos. 
  # Crear un array B con el precio de cada producto. 
  # Es decir en la posición 0 del array B deberá almacenarse 
  # el precio del producto almacenado en la posición 0 del array B.

  import array

  nombreProducto =0
  precioProducto =0

  idProducto = 0

  # arrayNombre = array.array('u',[])
  listaNombre = []

  arrayPrecio = array.array('f',[])



  for i in range(1,11):
    listaNombre.append(input("Ingrese nombre del producto "))
    arrayPrecio.append(int(input("Ingrese el precio del producto ")))
    print()



  if(len(listaNombre) == 10 and len(arrayPrecio) == 10):
    print("============")
    print("Id  Nombre ")
    print("============")
    for j in range(1,11):
      print(f"{j}   {listaNombre[j-1]} ")
    
    print()
    idProducto = int(input("Digite el Id del producto"))
    print()

  for m in range(1,len(arrayPrecio)+1):
    m =  idProducto
    print(f"El producto {listaNombre[m-1]} Tiene un precio de: ${arrayPrecio[m-1]}")
    break

  print()
  # print(f"nombre del los productos son: {listaNombre}")
  # print(f"nombre del los productos son: {arrayPrecio}")


def eje3():
  # 3.	Llenar un array de 20 elementos, imprimir la 
  # posición y el valor del elemento mayor almacenado
  # en la lista. Suponga que todos los elementos del array son diferentes.

  import array
  from random import randrange

  elementos = array.array('b',[])
  mayor =0 
  posicionMayor = 0


  for i in range(1,21):
    # elementos.append(randrange(20))
    elementos.append(i)
    if(i == 1):
      mayor = elementos[i-1]
      posicionMayor = i


    if( elementos[i-1] > mayor):
      mayor = elementos[i-1]
      posicionMayor = i
      
  print(elementos)
  print(f"El elemento mayor es {mayor}, esta en la Posicion {posicionMayor}")
  print()




def eje4():
  # 4.	Almacenar 300 números en un array, imprimir 
  # cuantos son ceros, cuántos son negativos,
  # cuantos positivos. Imprimir además la suma 
  # de los negativos y la suma de los positivos.

  import array
  from random import randrange

  arrayNumeros = array.array('b',[])
  contadorCeros = 0
  contadorPositivos = 0
  contadorNegativos = 0

  sumaPositivos = 0
  sumaNegativos = 0

  cantidad = 300



  for i in range(cantidad):
      arrayNumeros.append(randrange(-8,8))

      if(arrayNumeros[i] == 0):
        contadorCeros = contadorCeros + 1
      
      if(arrayNumeros[i] > 0):
        contadorPositivos = contadorPositivos + 1
        sumaPositivos = sumaPositivos + arrayNumeros[i]
      elif(arrayNumeros[i] < 0):
        contadorNegativos = contadorNegativos + 1
        sumaNegativos = sumaNegativos + arrayNumeros[i]
      



  print(arrayNumeros)
  print()
  print(f"la cantidad de cerso son {contadorCeros}")
  print(f"la cantidad de positivos son {contadorPositivos}")
  print(f"la cantidad de Negativos son {contadorNegativos}")
  print(f"la suma de los positivos  son {sumaPositivos}")
  print(f"la suma de los negativos  son {sumaNegativos}")



def eje5():
  # 5. Diseñe un algoritmo que lea un número cualquiera y 
  # lo busque en el array o vector X, el cual tiene
  # almacenados 80 elementos. Escribir la posición 
  # donde se encuentra almacenado el número en
  # el vector o el mensaje “NO” si no lo encuentra.


  import array
  from random import randrange

  numero =0
  posicionEncontrada =0
  numeroEncontrado =0
  noEncontrado =-1
  arrayBuscarNumero = array.array('b',[])



  for i in range(80):
    arrayBuscarNumero.append(randrange(0,80))
    
  numero = int(input("Ingrese un numero para buscar "))
  print()

  for j in range(len(arrayBuscarNumero)):

    while(numero == arrayBuscarNumero[j] ):
      print(f"numero encontrado siii {numero} en la posicion {j} ")
      print()
      posicionEncontrada = j
      numeroEncontrado = arrayBuscarNumero[j]
      break


    # if(numero == arrayBuscarNumero[j]):
    #   posicionEncontrada = j
    #   numeroEncontrado = arrayBuscarNumero[j]
    #   print("Numero contrado")
      
    # else:
    #   print(f"El numero {numero} No fue encontrado... ")
    #   noEncontrado = 0
      
  if(numeroEncontrado == 0):
    print(f"No se encontro el numero {numero}")
    print()
      



  # for m in range(len(arrayBuscarNumero)):
  #   print(arrayBuscarNumero[m])
  # # print(arrayBuscarNumero)

  # if(noEncontrado == 1):
  #   print(f"El numero encontrado es: {numeroEncontrado}")
  # else:
  #   print(f"No se encontro el numero: {numero}")

  print(arrayBuscarNumero)

def eje6():

  # 6. Diseñe un algoritmo que lea dos arrays o 
  # vectores A y B de 20 elementos cada uno y multiplique el
  # primer elemento de A con el último elemento de B 
  # y luego el segundo elemento de A por el
  # diecinueveavo elemento de B y así sucesivamente 
  # hasta llegar al veinteavo elemento de A por el
  # primer elemento de B. El resultado de la multiplicación 
  # almacenarlo en un vector C.


  import array

  arrayA = array.array('b',[])
  arrayB = array.array('b',[])
  arrayC = array.array('b',[])

  arrayAux = array.array('b',[])

  # Llenado de arrays
  for i in range(20):
    arrayA.append(i)
    arrayB.append(i)

  # invertir array
  for inter in range(20,0,-1):
    arrayAux.append( arrayA[inter-1])

  # multiplicar arrays
  for j in range(len(arrayAux)):
    arrayC.append(arrayAux[j] * arrayB[j])


  print(arrayA)
  print(arrayAux)
  print()
  print("Array resultante :")
  print(arrayC)



def eje7():

  # 7.	Se tiene 4 vectores mostrar el menor valor. (condicionales Anidados)``

  import array
  from random import random, randrange

  arrayUno = array.array('b',[])
  arrayDos = array.array('b',[])
  arrayTres = array.array('b',[])
  arrayCuatro = array.array('b',[])

  menorUno =0
  menorDos =0
  menorTres =0
  menorCuatro =0

  for i in range(4):
      arrayUno.append(randrange(10))
      arrayDos.append(randrange(10))
      arrayTres.append(randrange(10))
      arrayCuatro.append(randrange(10))


  if(len(arrayUno) == len(arrayDos) and len(arrayTres) == len(arrayCuatro) and len(arrayDos) == len(arrayTres)):
      for j in range(len(arrayUno)):
          if(j == 0):
              menorUno = arrayUno[j]
              menorDos = arrayDos[j]
              menorTres = arrayTres[j]
              menorCuatro = arrayCuatro[j]
          
          
          if(menorUno > arrayUno[j]):
              menorUno = arrayUno[j]

          if(menorDos > arrayDos[j]):
              menorDos = arrayDos[j]

          if(menorTres > arrayTres[j]):
              menorTres = arrayTres[j]

          if(menorCuatro > arrayCuatro[j]):
              menorCuatro = arrayCuatro[j]

          



  print(arrayUno)
  print(arrayDos)
  print(arrayTres)
  print(arrayCuatro)
  print()


  if(menorUno < menorDos and menorUno < menorTres and menorUno < menorCuatro):
      print(f"El menor es {menorUno}")
  elif(menorDos < menorTres and menorDos < menorCuatro):
      print(f"El menor es {menorDos}")
  elif(menorTres < menorCuatro):
      print(f"El menor es {menorTres}")
  else:
      print(f"El menor es {menorCuatro}")





menu = '''
Digite la opcion numerica del menú \n
    1) En un array no se pueden almacencar diferentes tipos de valores, se debe hacer en diferentes array (listas)
    2) Ejercicio 2
    3) Ejercicio 3
    4) Ejercicio 4
    5) Ejercicio 5
    6) Ejercicio 6
    7) Ejercicio 7
    0) Salir 

    '''

op = ""

while(op != 0):
    op = int(input(menu))

    
    if(op == 2):
        eje2()
    elif(op == 3):
        eje3()
    elif(op == 4):
        eje4()
    elif(op == 5):
        eje5()
    elif(op == 6):
        eje6()
    elif(op == 7):
        eje7()




