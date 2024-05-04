def punto1(TALLERLISTAS):
    print("En una lista en python si se pueden almacenar valores de diferente tipo :)")

datos=[]
def punto2  (TALLERLISTAS):
    nombre=str(input("Ingrese su nombre: " ))
    datos.append(nombre)
    ed=str(input("Ingrese su edad: " ))
    datos.append(ed)
    tel=str(input("Ingrese su telefono: " ))
    datos.append(tel)
    direcc=str(input("Ingrese su direccion: " ))
    datos.append(direcc)
    corr=str(input("Ingrese su correo: " ))
    datos.append(corr)
    print(datos)


def punto3  (TALLERLISTAS):
    Nombres = []
    for i in range (15):
        N=str(input("Ingrese nombre: "))
        Nombres.append(N)
    Nombres.sort()
    print(Nombres)

def punto4 (TALLERLISTAS):
    n=[]

    e=int(input("Digite la cantidad de numeros que quiere ingresar: "))
    for i in range (e):
        k=int()(input("ingrese un numero: "))
        n.append(k)
    print(n)


def punto5 (TALLERLISTAS):

    promedio=[]
    suma=0
    cantidad=0

    for l in range (1, 51):
        m=int(input("ingrese el valor de un numero: "))
        promedio.append(m)
        suma=sum(promedio)
    print(promedio)
    print(suma/l)

edad=[]
def punto6 (TALLERLISTAS):
    contmy=0
    contmn=0
    print("Para detener el ingreso de edades ponga: 0 ")

    l=int(input(("Ingrese edades: ")))
    edad.append(l)
    while l!=0:
        l=int(input(("Ingrese edades : ")))
        edad.append(l)
    for i in range (len(edad)):

            if edad[i]>=18:
                contmy=contmy+1

            if edad[i]<18:
                if edad[i]!=0:
                    contmn=contmn+1
                else:
                    contmn=contmn

    print("Estos son el numero de personas que son mayores de edad: ",contmy)
    print("Estos son el numero de personas que son menores de edad: ",contmn)


def punto7 (TALLERLISTAS, punto6):
    punto6(TALLERLISTAS)
    edadmayor=[]
    edadmenor=[]

    for i in range (len(edad)):
        if edad[i]>=18:
            edadmayor.append(i)
        if edad[i]<18:
            if edad[i]!=0:
                edadmenor.append(i)
    print(edadmayor)
    print(edadmenor)


def punto8 (TALLERLISTAS):
    a=[]
    b=[]
    resultado=[]
    r=0

    t=int(input("Cuantos numeros desea inresar a la lista a cada lista : "))

    for e in range (1,t+1):
        x=int(input("Ingrese un número a la lista A: "))
        a.append(x)
        d=int(input("Ingrese un número a la lista B: "))
        b.append(d)

    for i in range (t):
        r=a[i]+b[i]
        resultado.append(r)
    print("EL resultado de la suma de las dos listas es: ",resultado)


def punto9 (TALLERLISTAS):

    nombres=[]
    notaalgoritmo=[]
    notaingles=[]
    notadatos=[]
    totalnota=[]
    suma=0 
    t=[]
    w=0
    l=0
    u=0


    cantidad=int(input("Ingrese la cantidad de estudiantes para ingresar nota: "))
    for x in range (1,cantidad+1):
        n=str(input("Ingrese el nombre del estudiante: "))
        nombres.append(n)
        i=float(input("Ingrese nota de ingles del estudiante: "))
        notaingles.append(i)
        b=float(input("Ingrese nota de base de datos del estudiante: "))
        notadatos.append(b)
        a=float(input("Ingrese la nota de algoritmo del estudiante: "))
        notaalgoritmo.append(a)
    for e in range (2):
            suma=notaalgoritmo[e]+notadatos[e]+notaingles[e]
            totalnota.append(suma)
            t=totalnota[(e)]/3
    print(nombres,notaalgoritmo,notaingles,notadatos)

    w=sum(notaalgoritmo)
    l=sum(notaingles)
    u=sum(notadatos)

    for r in range (cantidad):
        print(f"El promedio de las notas de {nombres[r]} es: ",totalnota[r]/3)
    print("Este es el promedio de la Materia de Algoritmo : ",w/cantidad)
    print("Este es el promedio de la Materia de Ingles : ",l/cantidad)
    print("Este es el promedio de la Materia de Base de datos  : ",u/cantidad)

TALLERLISTAS=int(input(" PUNTOS DEL TALLER LISTA, SELECCIONALOS :\n 1.\n 2.\n 3.\n 4.\n 5.\n 6.\n 7.\n 8.\n 9.\n 10.\n Ingrese el punto que desea ejecutar: "))

if TALLERLISTAS ==1:
    punto1(TALLERLISTAS)

if TALLERLISTAS == 2:
    punto2(TALLERLISTAS)

if TALLERLISTAS == 3:
    punto3(TALLERLISTAS)

if TALLERLISTAS == 4:
    punto4(TALLERLISTAS)

if TALLERLISTAS == 5:
    punto5(TALLERLISTAS)

if TALLERLISTAS == 6:
    punto6(TALLERLISTAS)

if TALLERLISTAS ==7:
    punto7(TALLERLISTAS,punto6)

if TALLERLISTAS ==8:
    punto8(TALLERLISTAS)

if TALLERLISTAS == 9:
    punto9(TALLERLISTAS)

if TALLERLISTAS ==10:
    print("HAS SALIDO DEL PROGRAMA  ")