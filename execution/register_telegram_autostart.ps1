# Ejecutar una sola vez para que el bridge de Telegram arranque solo
# cada vez que inicies sesión en este ordenador. No requiere permisos
# de Administrador (la tarea se registra para el usuario actual).
#
# Uso:  powershell -ExecutionPolicy Bypass -File register_telegram_autostart.ps1

$taskName  = "Agente IA - Telegram Bridge"
$scriptDir = $PSScriptRoot
$vbsPath   = Join-Path $scriptDir "start_telegram_hidden.vbs"

if (-not (Test-Path $vbsPath)) {
    Write-Host "No encuentro $vbsPath. Ejecuta este script desde la carpeta execution/ del proyecto." -ForegroundColor Red
    exit 1
}

Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue

$action   = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "`"$vbsPath`""
$trigger  = New-ScheduledTaskTrigger -AtLogOn
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
            -ExecutionTimeLimit ([TimeSpan]::Zero) -MultipleInstances IgnoreNew

try {
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null
} catch {
    Write-Host "No se pudo registrar la tarea: $_" -ForegroundColor Red
    Write-Host "Prueba a ejecutar PowerShell como Administrador y repite el comando." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Listo. La tarea '$taskName' arrancara el bridge cada vez que inicies sesion." -ForegroundColor Green
Write-Host "Para arrancarlo ahora mismo sin reiniciar: doble clic en start_telegram_hidden.vbs"
Write-Host "Para comprobar que esta activa: schtasks /query /tn `"$taskName`""
Write-Host "Para desactivarla: Unregister-ScheduledTask -TaskName `"$taskName`""
