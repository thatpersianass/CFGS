/* 1.D. Crea un usuario para la base de datos creada llamado ‘user_tu_nombre’ y con la clave
‘12345’.*/

CREATE USER user_marcosj IDENTIFIED BY '12345';

/* 2.D. Otorgar al usuario creado user_tu_nombre, los privilegios de inserción y borrado sobre todas
las tablas de la BD.*/
GRANT INSERT, DELETE ON proyectos TO user_marcosj;

SHOW GRANTS FOR user_marcosj;

/* 3.D. Crear un segundo usuario llamado "po_tu_nombre" que tenga permisos sólo de consulta
sobre los campos FechaAsignación y FechasLimite de la tabla Tareas; y permisos de actualización
del campo PorcentajeAvance de la tabla Avances_Tareas.*/

CREATE USER po_marcosj IDENTIFIED BY 'diablo';

GRANT SELECT (FechaAsignacion) ON proyectos.tareas TO po_marcosj;
GRANT UPDATE (FechaLimite) ON proyectos.tareas TO po_marcosj;

GRANT UPDATE (PorcentajeAvance) ON proyectos.avances_tareas TO po_marcosj;