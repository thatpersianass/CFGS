#!/bin/bash
# Crea un script en bash con las siguientes opciones:
#     1. Cambio de propietario y grupo. Solicitar la ruta de un archivo y el nombre del nuevo
#     grupo y propietario. Cambiar el propietario del grupo del archivo. (1,5 ptos)
#     2. Solicitar el nombre de un usuario y mostrar la información del archivo /etc/passwd
#     filtrada por ese nombre de usuario. (1 pto)

echo "Menu Ejercicio 4:"
echo "  1. Cambiar propietario y grupo"
echo "  2. Ver /et/passwd de un usuario"
echo "  3. Salir"
read -p "-->  " opt

if [$opt -eq 1]
then
    read -p "Introduzca la ruta ABSOLUTA del archivo:" ruta
    read -p "Introduzca el nombre del nuevo propietario:" propietario
    read -p "Introduzca el nombre del nuevo grupo:" grupo

    if [ -f "$ruta" ]
    then
        chown "$propietario:$grupo" "$ruta"
        echo "Cambios realizados con éxito."
    else
        echo "El archivo no existe"
        fi

elif [$opt -eq 2]
then
    read -p "Introduzca el nombre de un usuario:" usuario

    grep "^$usuario:" /etc/passwd > /dev/null

    if [ $? -eq 0 ]
    then
        grep "^$usuario:" /etc/passwd
    else
        echo "El usuario no existe en /etc/passwd"
fi