"""
3. (2 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
- La función que vas a crear va a capturar, la edad, nombre de un alumnos y la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""


import datetime

def conteo(funcion):
    def funcion_inter(*args):
        print("Cantidad de parámetros", len(args))
        if len(args) > 1:
            funcion(*args)
            print("La funcion fue ejecutada")
        else:
            print("Debe haber más de un parámetro")
    return funcion_inter

def alumnos(nombre, edad, hora, minuto, nota1, nota2, nota3, nota4):
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print("{} de {} años ha sido registrado a las {} horas con {} minutos".format(nombre, edad, hora, minuto))
    print("Promedio del estudiante:", promedio)

nombre = input("Ingrese el nombre del alumno: ")
edad = int(input("Ingrese la edad: "))

hora = int(input("Ingrese la hora: "))
minuto = int(input("Ingrese los minutos: "))

nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))
nota4 = float(input("Ingrese nota 4: "))

alumnos(nombre, edad, hora, minuto, nota1, nota2, nota3, nota4)
