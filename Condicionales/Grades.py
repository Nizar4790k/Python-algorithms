"""
1. Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara
si su promedio de tres calificaciones es mayor o igual a 10.5; reprueba en caso
contrario.
"""

grade1 = float(input("Ingrese la calificacion 1: "))
grade2 = float(input("Ingrese la calificacion 2: "))
grade3 = float(input("Ingrese la calificacion 3: "))

avg = (grade1 + grade2 + grade3)/3

if avg>=10.5:
    print("Aprobado")
else:
    print("Reprobado")

