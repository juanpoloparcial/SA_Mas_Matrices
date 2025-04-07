print("- Notas de los alumnos -\n")

alumnos = [
    ['Juan', [['Matematicas', 8], ['Lengua', 9], ['Sociales', 7], ['Naturales', 7]]],
    ['Ana', [['Lengua', 9], ['Matematicas', 10], ['Sociales', 8], ['Naturales', 6]]],
    ['Luis', [['Lengua', 6], ['Sociales', 8], ['Matematicas', 7], ['Naturales', 6]]],
    ['María', [['Lengua', 9], ['Sociales', 10], ['Naturales', 10], ['Matematicas', 9]]]
]

def buscar_alumno(nombre):
    for alumno in alumnos:
        if alumno[0].lower() == nombre.lower():
            return alumno
    return None

while True:
    print("\n--- Sistema de Calificaciones ---")
    nombre = input("Nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        # Cuando el usuario elija esta opción, termina la ejecución del programa
        # y muesta la lista completa. Se haya editado o no.
        break

    alumno = buscar_alumno(nombre)

    if alumno:
        print(f"{nombre} ya está registrado.")
        materia = input("Nombre de la materia: ")
        nota = int(input("Nota: "))

        # Buscamos la materia.
        materias = alumno[1]
        for m in materias:
            if m[0].lower() == materia.lower():
                m[1] = nota
                print(f"Nota de {materia} actualizada.")
                break
        else:
            materias.append([materia, nota])
            print(f"Materia {materia} agregada.")
    else:
        materias = []
        for _ in range(4):
            materia = input("Materia: ")
            nota = int(input("Nota: "))
            materias.append([materia, nota])
        alumnos.append([nombre, materias])
        print(f"Alumno {nombre} agregado.")

# Se muestra la lista de alumnos con sus notas correspondientes
print("\n--- Datos Finales ---")
for alumno in alumnos:
    print(f"{alumno[0]}: {alumno[1]}")
