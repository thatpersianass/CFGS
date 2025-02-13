# Crea un script con PowerShell muestre un menú con opciones para gestionar procesos:
#     1. Filtrar Procesos por CPU: Mostrar los procesos que consumen más del 1% de CPU.
#     0,625 ptos
#     2. Procesos por Consumo de Memoria: Mostrar el nombre, ID y porcentaje de CPU de
#     los procesos ordenados por consumo de memoria (de mayor a menor). 0,625 ptos
#     3. Matar Proceso: Solicitar el ID de un proceso y finalizarlo. 0,625 ptos
#     4. Salir. 0,625 ptos (Más funcionamiento general)
# El script se debe repetir hasta que el usuario introduzca la opción Salir

# Muestra el menú de opciones
while ($true) {
    Write-Host ""
    Write-Host "Gestion de Procesos:"
    Write-Host "    1. Filtrar Procesos por CPU"
    Write-Host "    2. Procesos por Consumo de Memoria"
    Write-Host "    3. Matar Proceso"
    Write-Host "    Escriba SALIR para cerrar el programa"

    $option = Read-Host "   -->  "
    switch ($option) {
        "1" {
            # Filtrar Procesos por CPU
            $cpuThreshold = 0.0125
            $cpuConsumingProcesses = Get-Process | Where-Object { $_.CPU -gt $cpuThreshold }
            Write-Host "Procesos consumiendo más del 1% de CPU:"
            foreach ($process in $cpuConsumingProcesses) {
                Write-Host "ID: $($process.Id), Nombre: $($process.Name), CPU: $($process.CPU)"
            }
        }
        
        "2" {
            # Procesos por Consumo de Memoria
            $memoryConsumingProcesses = Get-Process | Sort-Object -Property WS -Descending
            Write-Host "Procesos ordenados por consumo de memoria (de mayor a menor):"
            foreach ($process in $memoryConsumingProcesses) {
                Write-Host "ID: $($process.Id), Nombre: $($process.Name), CPU: $($process.CPU), Memoria: $($process.WS / 1MB) MB"
            }
        }

        "3" {
            # Matar Proceso
            $processId = Read-Host "Introduzca el ID del proceso a matar:"
            Stop-Process -Id $processId -Force
            Write-Host "Proceso $processId detenido exisosamente."
        }

        "SALIR" {exit}
        default { Write-Host "Opcion no valida, intente de nuevo." }
    }
}