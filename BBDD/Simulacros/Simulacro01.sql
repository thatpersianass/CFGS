-- 1. Devuelve un listado con los datos de todas las alumnas que se han matriculado alguna vez
-- en el Grado en Ingeniería Informática

SELECT DISTINCT P.nombre AS Nombre, G.id AS ID_GRADO, G.nombre AS GRADO
FROM alumno_se_matricula_asignatura AS AA
JOIN persona P ON AA.id_alumno = P.id
JOIN asignatura A ON AA.id_asignatura = A.id
JOIN grado G ON G.id = A.id_grado
WHERE P.sexo = "M" and G.id = 4;

-- 2. Devuelve un listado de los profesores junto con el nombre del departamento al que están
-- vinculados. El listado debe devolver cuatro columnas, primer apellido, segundo apellido,
-- nombre y nombre del departamento. El resultado estará ordenado alfabéticamente de menor a
-- mayor por los apellidos y el nombre.
SELECT P.apellido1 AS primer_apellido, P.apellido2 AS segundo_apellido, P.nombre AS nombre, D.nombre AS nombre_departamento
FROM profesor PR
JOIN persona P ON P.id = PR.id_profesor
JOIN departamento D ON D.id = PR.id_departamento
ORDER BY P.apellido1, P.apellido2, P.nombre ASC;

-- 3. Devuelve un listado con el nombre de todos los departamentos que tienen profesores que
-- imparten alguna asignatura en el Grado en Ingeniería Informática (Plan 2015). 
SELECT D.nombre AS nombre_departamento, A.nombre as nombre_asignatura
FROM profesor PR
JOIN departamento D ON D.id = PR.id_departamento
JOIN asignatura A ON PR.id_profesor = A.id_profesor
JOIN grado G ON G.id = A.id_grado;

-- 4.- Devuelve un listado con todos los alumnos que se han matriculado en alguna asignatura
-- durante el curso escolar 2018/2019. 
SELECT distinct P.nombre AS nombre_alumno, C.anyo_inicio AS ANIO_INICIO, C.anyo_fin AS ANIO_FIN
FROM alumno_se_matricula_asignatura AA
JOIN persona P ON P.id = AA.id_alumno
JOIN curso_escolar C ON C.id = AA.id_curso_escolar
WHERE C.anyo_inicio = 2018;

-- 6.- Devuelve un listado con los departamentos que no tienen profesores asociados
SELECT DISTINCT D.nombre AS nombre_departamento
FROM profesor P
LEFT JOIN departamento D ON P.id_departamento = D.id
WHERE P.id_departamento IS null;

-- 7. Devuelve un listado con todos los departamentos que tienen alguna asignatura que no se
-- haya impartido en ningún curso escolar. El resultado debe mostrar el nombre del
-- departamento y el nombre de la asignatura que no se haya impartido nunca. 
SELECT D.nombre AS nombre_departamento
FROM alumno_se_matricula_asignatura AA
JOIN curso_escolar C ON AA.id_curso_escolar = C.id
JOIN asignatura A ON AA.id_asignatura = A.id
JOIN profesor P ON A.id_profesor = P.id_profesor
JOIN departamento D ON P.id_departamento = D.id
WHERE C.id IS NULL;

-- 13.- Devuelve todos los datos del alumno más joven.
SELECT *
FROM persona
WHERE tipo = "Alumno"
ORDER BY fecha_nacimiento DESC
LIMIT 1;