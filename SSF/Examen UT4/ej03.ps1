$cpuLimit = 40  # Porcentaje de CPU que queremos utilizar
$interval = 1    # Intervalo de tiempo en segundos

while ($true) {
    $start = Get-Date
    # Realiza una operación que consume CPU de forma simple
    while ((Get-Date) - $start -lt (New-TimeSpan -Seconds $interval)) {
        $dummy = "cargando..."
    }
    
    # Pausa para reducir el uso de la CPU
    Start-Sleep -Seconds ($interval * (100 - $cpuLimit) / 100)
}
$cpuLimit = 40  # Porcentaje de CPU que queremos utilizar
$interval = 1    # Intervalo de tiempo en segundos

while ($true) {
    $start = Get-Date
    # Realiza una operación que consume CPU de forma simple
    while ((Get-Date) - $start -lt (New-TimeSpan -Seconds $interval)) {
        $dummy = "cargando..."
    }
    
    # Pausa para reducir el uso de la CPU
    Start-Sleep -Seconds ($interval * (100 - $cpuLimit) / 100)
}
