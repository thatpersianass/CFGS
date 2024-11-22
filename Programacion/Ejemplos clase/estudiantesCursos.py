# Desarrolla un programa que sugiera cursos a estudiantes basándose en sus intereses y en la oferta de cursos disponibles.

# Recomendaciones:  
# Luis: {'Curso1', 'Curso2'}
# Ana: {'Curso1', 'Curso3'}
# Juan: {'Curso4'}

estudiantes = {
    "Luis": {"Python", "Data Science", "Machine Learning"},
    "Ana": {"Ciberseguridad", "Redes", "Python"},
    "Juan": {"Diseño", "Frontend", "React"}
}
cursos = {
    "Curso1": {"Python", "Introducción a la programación"},
    "Curso2": {"Data Science", "Estadística"},
    "Curso3": {"Ciberseguridad", "Hacking ético"},
    "Curso4": {"Frontend", "React", "JavaScript"}
}

sugerencias = {}

# for estudiante, intereses in estudiantes.items():
#     sugerencias[estudiante] = set()
#     for curso, temas in cursos.items():
#         for interes in intereses:
#             if interes in temas:
#                 sugerencias[estudiante].add(curso)
#                 break

# for estudiante, cursos_sugeridos in sugerencias.items():
#     print(f"{estudiante}: {cursos_sugeridos}")

for estudiante in estudiantes:
    curso_est = set()
    for curso in cursos:
        if  estudiantes[estudiante].intersection(cursos[curso]):
            curso_est.add(curso)

print(curso_est)