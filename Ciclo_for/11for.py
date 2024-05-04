"""Se desea conocer una serie de datos de una empresa con 50 empleados: 
a.	¿Cuántos empleados ganan más de 3.000.000 pesos al mes (salarios altos);
b.	entre 1.500.000 y 3.000.000 pesos (salarios medios);
c) menos de 1.500.000 pesos (salarios bajos y empleados a tiempo parcial)? """

e=0
salariosAltos=0
salariosMedios=0
salariosBajos=0

for i in range (50):
    e=int(input(f"Digite salario del empleado{i+1}: "))
    if e > 3000000:
        salariosAltos+=1
    if e>=1500000 and e<=3000000:
        salariosMedios+=1
    if e<1500000:
        salariosBajos+=1
print("Estos son los numero de empleados que tienen un salario alto: ",salariosAltos)
print("Estos son los numero de empleados que tienen un salario medio: ",salariosMedios)
print("Estos son los numero de empleados que tienen un salario bajo: ",salariosBajos)








