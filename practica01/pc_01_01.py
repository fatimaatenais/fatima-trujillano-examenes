"""
1.- Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:

- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""
# 1
nombre = "Fátima"
salario = 6000
edad = "17"
compania = "GOOGLE"

print("Nombre:", nombre, "tipo:", type(nombre))
print("Salario:", salario, "tipo:", type(salario))
print("Edad:", edad, "tipo:", type(edad))
print("Compania:", compania, "tipo:", type(compania))

# 2

conv_edad = int(edad)

# 3
if conv_edad > 30:
    bono_porcentaje = 0.10
    print("Usted tiene un bono de 10% en el mes de diciembre")

else:
    bono_porcentaje = 0.05
    print("Usted tiene un bono del 5% en el mes diciembre")

# 4
potencia_salario = salario ** 2
bono_extra = salario * bono_porcentaje
bono_final = potencia_salario + bono_extra

print("El bono final es:", bono_final)





