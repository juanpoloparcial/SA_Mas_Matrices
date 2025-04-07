console.log("Notas de los Alumnos y sus materias.")

let alumnos = [
    ['Juan', [['Matematicas', 8], ['Lengua', 9], ['Sociales', 7], ['Naturales', 7]]],
    ['Ana', [['Lengua', 9], ['Matematicas', 10], ['Sociales', 8], ['Naturales', 6]]],
    ['Luis', [['Lengua', 6], ['Sociales', 8], ['Matematicas', 7], ['Naturales', 6]]],
    ['María', [['Lengua', 9], ['Sociales', 10], ['Naturales', 10], ['Matematicas', 9]]]
];

function buscarAlumno(nombre) {
    return alumnos.find(alumno => alumno[0].toLowerCase() === nombre.toLowerCase());
}

// Simulación en la consola
function agregarOModificarAlumno(nombre, materia, nota) {
    let alumno = buscarAlumno(nombre);

    if (alumno) {
        console.log(`${nombre} ya está registrado.`);
        let materias = alumno[1];
        let materiaEncontrada = materias.find(m => m[0].toLowerCase() === materia.toLowerCase());
        if (materiaEncontrada) {
            materiaEncontrada[1] = nota;
            console.log(`Nota de ${materia} actualizada a ${nota}.`);
        } else {
            materias.push([materia, nota]);
            console.log(`Materia ${materia} agregada con nota ${nota}.`);
        }
    } else {
        alumnos.push([nombre, [[materia, nota]]]);
        console.log(`Alumno ${nombre} agregado con materia ${materia}.`);
    }
}

// Ejemplo de uso:
agregarOModificarAlumno("Juan", "Lengua", 10);
agregarOModificarAlumno("Sofía", "Matematicas", 9);
agregarOModificarAlumno("Joker", "Matematica", 10);
console.log(alumnos);
