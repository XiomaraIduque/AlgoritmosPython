"""Generar los primeros 50 números primos positivos."""
#  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61,
#  67. 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
#  137, 139, 149, 151, 157, 163,  167, 173, 179, 181, 191, 193,
#  197, 199, 211, 223, 227, 229

numero=0


for i in range (2,230):
    contador=0
    for a in range (1,i):
        if i%a==0:
            contador=contador+1
    if contador<=2:
            print(i)
