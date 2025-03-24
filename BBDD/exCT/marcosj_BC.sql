/* 1.B. Añadir las restricciones correspondientes para que en la tabla Proyectos, la fecha de encargo
no pueda ser anterior al año 2025 ni posterior a la fecha de entrega del proyecto; y además que el
importe del presupuesto no pueda ser inferior a 1.000€ ya que esa es la cantidad mínima que
cobra la empresa por los estudios iniciales de viabilidad. */
USE proyectos;

ALTER TABLE PROYECTOS
ADD CONSTRAINT CHK_fecha_encargo CHECK (YEAR(FechaInicio) >= 2025 AND FechaInicio <= FechaEntrega),
ADD CONSTRAINT CHK_presupuesto CHECK (Presupuesto >= 1000);

/* 2.B. Añade una columna en la tabla Proyectos llamada “revision_prespuesto”, justo después de
la columna presupuesto, que registrará el presupuesto inicial con un aumento del 15%. */

ALTER TABLE PROYECTOS 
ADD COLUMN revision_presupuesto INT NOT NULL AFTER Presupuesto;

UPDATE PROYECTOS 
SET revision_presupuesto = ROUND(Presupuesto * 1.15);

/* 1.C. Crea una vista para calcular el promedio de avance de cada proyecto. Utiliza esta vista para
mostrar aquellos proyectos que deban finalizar antes del 2025 y que tengan un promedio de
avance mayor al 50%. Debe mostrarse Id y nombre del proyecto, nombre del cliente, presupuesto,
fechas de inicio y entrega y el promedio del porcentaje de avance del proyecto. */

CREATE VIEW Prom_Proyectos AS
SELECT P.ProyectoID AS ID, NombreProyecto AS Nombre, C.NombreEmpresa AS Nombre_Cliente, Presupuesto, FechaInicio, FechaEntrega, COALESCE(AVG(A.PorcentajeAvance), 0) AS PromedioAvance
FROM proyectos P
JOIN clientes C ON P.ClienteID = C.CIF
LEFT JOIN AVANCES_TAREAS A ON P.ProyectoID = A.TareaID
GROUP BY P.ProyectoID;

/* 2.C. Crear una vista que calcule los días restantes para la finalización de las tareas de cada
proyecto. Utiliza esta vista para mostrar aquellos proyectos cuya fecha límite sea dentro de los
próximos 10 días (o menos). Debe mostrarse el ID de la tarea. el nombre del proyecto a que
pertenece, la descripción, el porcentaje de avance y la fecha límite.*/

CREATE VIEW dias_restantes AS
SELECT T.TareaID, P.NombreProyecto, T.Descripcion, COALESCE(AVG(A.PorcentajeAvance), 0) AS PromedioAvance, T.FechaLimite, DATEDIFF(T.FechaLimite, NOW()) AS DiasRestantes
FROM  tareas T
JOIN  proyectos P ON P.ProyectoID = T.ProyectoID
LEFT JOIN AVANCES_TAREAS A ON T.TareaID = A.TareaID
GROUP BY  T.TareaID, P.NombreProyecto, T.Descripcion, T.FechaLimite
WHERE DiasRestantes <= 10;