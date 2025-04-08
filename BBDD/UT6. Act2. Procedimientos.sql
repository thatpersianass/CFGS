-- 1. Crear un procedimiento que inserte un nuevo estudiante, reciba todos los campos como parámetros y verifique que el DNI no exista antes de la inserción.
DELIMITER //
CREATE PROCEDURE insertar_estudiante(
    IN p_nombre VARCHAR(100), IN p_apellido VARCHAR(100),
    IN p_dni VARCHAR(15), IN p_email VARCHAR(100))
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Estudiantes WHERE dni = p_dni) THEN
        INSERT INTO Estudiantes (nombre, apellido, dni, email)
        VALUES (p_nombre, p_apellido, p_dni, p_email);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El estudiante con ese DNI ya existe.';
    END IF;
END;
//

-- 2. Diseñar un procedimiento que actualice el estado de una matrícula a “Cancelada” si se ha formalizado después de marzo).
DELIMITER //
CREATE PROCEDURE cancelar_matriculas_fuera_de_plazo()
BEGIN
    UPDATE Matriculas SET estado = 'Cancelada' WHERE MONTH(fecha_matricula) > 3;
END;
//

-- 3. Generar un procedimiento que liste los estudiantes matriculados en un curso específico usando curso como parámetro de entrada.
DELIMITER //
CREATE PROCEDURE listar_estudiantes_por_curso(IN p_id_curso INT)
BEGIN
    SELECT e.id_estudiante, e.nombre, e.apellido, e.dni, e.email
    FROM Estudiantes e JOIN Matriculas m ON e.id_estudiante = m.id_estudiante
    WHERE m.id_curso = p_id_curso;
END;
//

-- 4. Crea un procediemiento que reciba como parámetro de entrada el identificador de un estudiante y como parámetro de salida una variable en la que se almacene el coste de todos los cursos en los que está matriculado.
DELIMITER //
CREATE PROCEDURE coste_total_estudiante(IN p_id_estudiante INT, OUT p_coste_total DECIMAL(10,2))
BEGIN
    SELECT SUM(c.coste) INTO p_coste_total
    FROM Cursos c JOIN Matriculas m ON c.id_curso = m.id_curso
    WHERE m.id_estudiante = p_id_estudiante;
END;
//

-- 5. Crear un procedimiento que reciba como parámetro de entrada el identificador de un curso y devuelva como parámetro de salida un mensaje indicando si aún hay plazas disponibles
-- o no (suponemos que el cupo máximo es 7 alumnos por curso)
DELIMITER //
CREATE PROCEDURE verificar_plazas_disponibles(IN p_id_curso INT, OUT p_mensaje VARCHAR(100))
BEGIN
    DECLARE total_matriculados INT;
    SELECT COUNT(*) INTO total_matriculados FROM Matriculas WHERE id_curso = p_id_curso;
    IF total_matriculados < 7 THEN
        SET p_mensaje = 'Sí, hay plazas disponibles.';
    ELSE
        SET p_mensaje = 'No hay plazas disponibles.';
    END IF;
END;
//

-- 6. Crea un procedimiento que admita un parámetro IN con el identificador de un curso y un parámetro INOUT para actualizar el coste del curso.
-- Este parámetro inicialmente contendrá el nuevo coste. El procedimiento debe comprobar, antes de hacer el cambio,
-- si ya hay alumnos matricuados en el curso; de ser así, no debe actualizar el coste.
DELIMITER //
CREATE PROCEDURE actualizar_coste_si_sin_matriculas(
    IN p_id_curso INT, INOUT p_nuevo_coste DECIMAL(10,2))
BEGIN
    DECLARE total_matriculados INT;
    SELECT COUNT(*) INTO total_matriculados FROM Matriculas WHERE id_curso = p_id_curso;
    IF total_matriculados = 0 THEN
        UPDATE Cursos SET coste = p_nuevo_coste WHERE id_curso = p_id_curso;
    ELSE
        SET p_nuevo_coste = NULL;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede actualizar el coste: hay estudiantes matriculados.';
    END IF;
END;
//
