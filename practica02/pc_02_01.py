"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):

Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.

- Calcular el promedio de cada estudiantes.

- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor

- Mostrar en pantalla el estudiante con mayor promedio
"""

def procesar_notas(estudiantes):
    resultado = {}
    mayor_prom = 0
    mejor_estudiant = ""

    for nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = sum(notas) / len(notas)

        if promedio >= 11:
            estado = "Estas aprobado!"
        else:
            estado = "Estas desaprobado"

        resultado[nombre] = {"promedio": promedio, "estado": estado}

        if promedio > mayor_prom:
            mayor_prom = promedio
            mejor_estudiant = nombre

    print("El estudiante que tuvo mayor promedio es: {} con {}".format(mejor_estudiant, f"{mayor_prom:.2f}"))
    return resultado

estudiantes = {"Almendra": [15, 10, 8], "Luana": [10, 9, 12], "Joaquin": [17, 16, 19]}

procesar_notas(estudiantes)






