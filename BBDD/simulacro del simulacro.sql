/* 1.- Devuelve un listado con los datos de todas las alumnas que se han matriculado alguna vez
en el Grado en Ingeniería Informática (Plan 2015).  */

SELECT DISTINCT P.nombre AS Nombre, G.id AS ID_GRADO, G.nombre AS GRADO
FROM alumno_se_matricula_asignatura AS AA
JOIN persona P ON AA.id_alumno = P.id
JOIN asignatura A ON AA.id_asignatura = A.id
JOIN grado G ON G.id = A.id_grado
WHERE P.sexo = "M" and G.id = 4;

/* 2.- Devuelve un listado de los profesores junto con el nombre del departamento al que están
vinculados. El listado debe devolver cuatro columnas, primer apellido, segundo apellido,
nombre y nombre del departamento. El resultado estará ordenado alfabéticamente de menor a
mayor por los apellidos y el nombre. */

SELECT p.apellido1, p.apellido2, p.nombre, d.nombre AS departamento
FROM persona p
JOIN profesor pr ON p.id = pr.id_profesor
JOIN departamento d ON pr.id_departamento = d.id
ORDER BY p.apellido1 ASC, p.apellido2 ASC, p.nombre ASC;

/*3.- Devuelve un listado con el nombre de todos los departamentos que tienen profesores que
imparten alguna asignatura en el Grado en Ingeniería Informática (Plan 2015).*/
SELECT DISTINCT d.nombre AS departamento
FROM departamento d
JOIN profesor pr ON d.id = pr.id_departamento
JOIN asignatura a ON pr.id_profesor = a.id_profesor
JOIN grado g ON a.id_grado = g.id
WHERE g.nombre = 'Grado en Ingeniería Informática (Plan 2015)';

/* 4.- Devuelve un listado con todos los alumnos que se han matriculado en alguna asignatura
durante el curso escolar 2018/2019 */

SELECT DISTINCT p.id, p.nombre, p.apellido1, p.apellido2
FROM persona p
JOIN alumno_se_matricula_asignatura am ON p.id = am.id_alumno
WHERE am.id_curso_escolar = 2018
AND p.tipo = 'alumno';

/* 5.- Devuelve un listado con los nombres de todos los profesores y los departamentos que
tienen vinculados. El listado también debe mostrar aquellos profesores que no tienen ningún
departamento asociado. El listado debe devolver cuatro columnas, nombre del departamento,
primer apellido, segundo apellido y nombre del profesor. El resultado estará ordenado
alfabéticamente de menor a mayor por el nombre del departamento, apellidos y el nombre. */
SELECT d.nombre AS departamento, p.apellido1, p.apellido2, p.nombre
FROM persona p
LEFT JOIN profesor pr ON p.id = pr.id_profesor
LEFT JOIN departamento d ON pr.id_departamento = d.id
WHERE p.tipo = 'profesor'
ORDER BY d.nombre ASC, p.apellido1 ASC, p.apellido2 ASC, p.nombre ASC;

/* 6.- Devuelve un listado con los departamentos que no tienen profesores asociados. */
SELECT d.nombre AS departamento
FROM departamento d
LEFT JOIN profesor pr ON d.id = pr.id_departamento
WHERE pr.id_profesor IS NULL;

/* 7.- Devuelve un listado con todos los departamentos que tienen alguna asignatura que no se
haya impartido en ningún curso escolar. El resultado debe mostrar el nombre del
departamento y el nombre de la asignatura que no se haya impartido nunca.  */
SELECT d.nombre AS departamento, a.nombre AS asignatura
FROM departamento d
JOIN profesor p ON d.id = p.id_departamento
JOIN asignatura a ON p.id_profesor = a.id_profesor
LEFT JOIN alumno_se_matricula_asignatura am ON a.id = am.id_asignatura
WHERE am.id_asignatura IS NULL;

/* 8.- Calcula cuántos profesores hay en cada departamento. El resultado sólo debe mostrar dos
columnas, una con el nombre del departamento y otra con el número de profesores que hay en
ese departamento. El resultado sólo debe incluir los departamentos que tienen profesores
asociados y deberá estar ordenado de mayor a menor por el número de profesores.  */
SELECT d.nombre AS departamento, COUNT(p.id_profesor) AS num_profesores
FROM departamento d
JOIN profesor p ON d.id = p.id_departamento
GROUP BY d.nombre
ORDER BY num_profesores DESC;

/* 9.- Devuelve un listado con todos los departamentos y el número de profesores que hay en
cada uno de ellos. Tenga en cuenta que pueden existir departamentos que no tienen
profesores asociados. Estos departamentos también tienen que aparecer en el listado. */
SELECT d.nombre AS departamento, COUNT(p.id_profesor) AS num_profesores
FROM departamento d
LEFT JOIN profesor p ON d.id = p.id_departamento
GROUP BY d.nombre
ORDER BY num_profesores DESC;

/* 10.- Devuelve un listado con el nombre de todos los grados existentes en la base de datos y el
número de asignaturas que tiene cada uno, de los grados que tengan más de 40 asignaturas
asociadas. */
SELECT g.nombre AS grado, COUNT(a.id) AS num_asignaturas
FROM grado g
JOIN asignatura a ON g.id = a.id_grado
GROUP BY g.nombre
HAVING COUNT(a.id) > 40
ORDER BY num_asignaturas DESC;
