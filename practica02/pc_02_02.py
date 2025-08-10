"""

2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""


def normalizar_nombres(nombres):
    lista_02 = []
    for nombre in nombres:
        nuevo_nombre = nombre.strip().title()
        partes = nuevo_nombre.split()

        for parte in partes:
            if parte not in lista_02:
                lista_02.append(parte)
    return lista_02

nombres = ["LUANA", " Almendra", "Joaquin Dulce", "Andres", "Mariana "]

resultado = normalizar_nombres(nombres)

print("lista original: {}".format(nombres))
print("Lista normalizada: {}".format(resultado))




