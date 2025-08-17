"""
2. Utilizar el concepto de módulo necesariamente. Y Escribir un programa
para el manejo de listas el cuál cumplirá los siguientes requerimientos (2
ptos):

Reglas:

- Crear una función que le permitirá almacenar X números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función. X solo
puede ser entero. No otro tipo de dato. Y también un índice existente en la
lista.

- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.

- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.

- Crear una función para indicar cuál es el mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.

- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo
"""


def almacenar_elemento():
    cantidad = int(input("¿Cuantos números quieres guardar?: "))
    lista = []

    for i in range(cantidad):
        numero = int(input("Ingrese un número :) => "))
        lista.append(numero)

    print("Lista hecha:", lista)
    return lista

def repetidos(lista):
    lista_02 = []
    for numero in lista:
        if numero not in lista_02:
            lista_02.append(numero)
    print("Lista con números sin repetir =>", lista_02)
    return lista_02

def ordenar(lista):

    lista.sort()
    print("Lista de menor a mayor:", lista)

    lista.sort()
    lista.reverse()
    print("Lista de mayor a menor", lista)

def mayor_par(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    if len(pares) > 0:
        mayor = pares[0]
        for numero in pares:
            if numero > mayor:
                mayor = numero
        print("El mayor numero par es:", mayor)
    else:
        print("No hay pares")

lista_terminada = almacenar_elemento()
lista_no_repetidos = repetidos(lista_terminada)
ordenar(lista_no_repetidos)
mayor_par(lista_no_repetidos)
