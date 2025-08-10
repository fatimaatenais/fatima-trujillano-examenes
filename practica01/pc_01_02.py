"""
2.Crear un entorno virtual y aplicar lo siguiente (4 ptos):
Reglas:
 - El nombre del entorno virtual tendrá el nombre con la siguiente estructura
 (apellido_nombre_edad)
 - Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
 aws (última versión)
 - Generar el archivo de requirements.txt (mostrar las librerías instaladas)
 - Crear un segundo archivo en el cual se creará una lista vacía, para luego
 agregar los datos de nombre, salario, edad, compañía y bono a esta lista vacía
 (todos estos datos ya fueron obtenidos en el problema anterior)
 - Caso: Reporte de calificaciones:
 Se tiene un alumno con calificaciones en tres cursos:
 Matemáticas: 17, Ciencia: 14, Historia: 15
"""

# Segundo archivo: REPORTE
from pc_01_01 import nombre, salario, edad, compania, bono_final

datos_completos = []

datos_completos.append(nombre)
datos_completos.append(salario)
datos_completos.append(edad)
datos_completos.append(compania)
datos_completos.append(bono_final)

matematicas = 17
ciencia = 14
historia = 15

calificaciones = {
    "Matemáticas": matematicas,
    "Ciencia": ciencia,
    "Historia": historia
}
datos_completos.append(calificaciones)

print("Datos del usuario + calificaciones:")
print(datos_completos)
