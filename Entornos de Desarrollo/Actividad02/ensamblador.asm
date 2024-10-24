section .data
    msg db "Me gusta la asignatura Entornos de Desarrollo :)", 0xA  ; Cadena de texto con un salto de línea
    len equ $ - msg  ; Longitud de la cadena

section .text
    global _start

_start:
    ; Escribir el mensaje
    mov eax, 4          ; sys_write
    mov ebx, 1          ; file descriptor 1 (salida estándar)
    mov ecx, msg        ; Dirección de la cadena a imprimir
    mov edx, len        ; Longitud de la cadena
    int 0x80            ; Llamada al sistema

    ; Salir del programa
    mov eax, 1          ; sys_exit
    xor ebx, ebx        ; Código de salida 0
    int 0x80            ; Llamada al sistema para salir
