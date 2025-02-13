#!/bin/bash
# En Ubuntu crea un script que reciba (no solicite) como parámetro una ruta:
#     a. En esa ruta se deberá crear la siguiente estructura de directorios: (0,5 ptos)

#     b. La carpeta documentos debe tener permisos de escritura lectura y ejecución
#     para el propietario, el grupo y el resto. (0,5 ptos)

#     c. La carpeta imágenes debe tener permisos de escritura y lectura para el
#     propietario y el grupo. (0,5 ptos)

#     d. La carpeta emails debe tener permisos de escritura lectura y ejecución solo
#     para el grupo. (0,5 ptos)

#     e. La carpeta cuentas debe tener permisos rwx solo para el propietario (0,5 ptos)

echo "ASEGURATE DE EJECUTAR EL SCRIPT EN MODO ROOT!"

mkdir $1/Documentos
mkdir $1/Documentos/Imagenes
mkdir $1/Documentos/emails
mkdir $1/Documentos/cuentas

chmod a+rwx $1/Documentos
chmod ug+rw $1/Documentos/Imagenes
chmod g+rwx $1/Documentos/emails
chmod u+rwx $1/Documentos/cuentas

echo "ARBOL DE DIRECTORIOS CREADO CON EXITO."