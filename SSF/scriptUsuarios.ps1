Clear-Host
Write-Host "1. Crear usuario"
Write-Host "2. Crear un grupo"
Write-Host "3. Añadir usuario a un grupo"
Write-Host "4. Establecer contraseña"
Write-Host "5. Deshabilitar cuenta"
Write-Host "6. Generar un informe"
Write-Host "7. Salir"

$Password = "P@ssword123"
New-LocalUser -Name "Ana.Garcia" -FullName "Ana García" -Password (ConvertTo-SecureString $Password -AsPlainText -Force) -Description "Contabilidad"
New-LocalUser -Name "Luis.Perez" -FullName "Luis Pérez" -Password (ConvertTo-SecureString $Password -AsPlainText -Force) -Description "Ventas"
New-LocalUser -Name "Maria.Rodriguez" -FullName "María Rodríguez" -Password (ConvertTo-SecureString $Password -AsPlainText -Force) -Description "Soporte Técnico"

New-LocalGroup -Name "Contabilidad"
New-LocalGroup -Name "Ventas"
New-LocalGroup -Name "Soporte Técnico"

Add-LocalGroupMember -Group "Contabilidad" -Member "Ana.Garcia"
Add-LocalGroupMember -Group "Ventas" -Member "Luis.Perez"
Add-LocalGroupMember -Group "Soporte Técnico" -Member "Maria.Rodriguez"

Set-LocalUser -Name "Maria.Rodriguez" -PasswordNeverExpires $true
Disable-LocalUser -Name "Luis.Perez"

while ($true) {
    $option = Read-Host "Seleccione una opción"
    switch ($option) {
        '1' { 
            $UserName = Read-Host "Ingrese el nombre de usuario"
            $FullName = Read-Host "Ingrese el nombre completo"
            $Password = Read-Host "Ingrese la contraseña" -AsSecureString
            $Description = Read-Host "Ingrese la descripción"
            New-LocalUser -Name $UserName -FullName $FullName -Password (ConvertTo-SecureString $Password -AsPlainText -Force) -Description $Description
        }
        '2' {
            $GroupName = Read-Host "Ingrese el nombre del grupo"
            New-LocalGroup -Name $GroupName
        }
        '3' {
            $UserName = Read-Host "Ingrese el nombre de usuario"
            $GroupName = Read-Host "Ingrese el nombre del grupo"
            Add-LocalGroupMember -Group $GroupName -Member $UserName
        }
        '4' {
            $UserName = Read-Host "Ingrese el nombre de usuario"
            $Password = Read-Host "Ingrese la nueva contraseña" -AsSecureString
            Set-LocalUser -Name $UserName -Password $Password
        }
        '5' {
            $UserName = Read-Host "Ingrese el nombre de usuario"
            Disable-LocalUser -Name $UserName
        }
        '6' {
            $Users = Get-LocalUser | Select-Object Name, Enabled, Description
            $Groups = Get-LocalGroup | Select-Object Name
            $Report = "Usuarios:\n" + ($Users | Out-String) + "\nGrupos:\n" + ($Groups | Out-String)
            foreach ($Group in $Groups) {
                $Members = Get-LocalGroupMember -Group $Group.Name | Select-Object Name
                $Report += "\nMiembros del grupo $($Group.Name):\n" + ($Members | Out-String)
            }
            $Report | Out-File "C:\Usuarios_Informe.txt"
            Write-Host "Informe generado en C:\Usuarios_Informe.txt"
        }
        '7' { exit }
        default { Write-Host "Opción no válida, intente de nuevo." }
    }
    Pause
}
