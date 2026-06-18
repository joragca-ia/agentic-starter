' Arranca el bridge de Telegram sin abrir ninguna ventana de consola.
' Pensado para lanzarse solo, vía el Programador de tareas de Windows
' (ver register_telegram_autostart.ps1). También se puede hacer doble
' clic en este archivo para arrancar el bridge manualmente.

Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c """ & scriptDir & "\start_telegram_bridge.bat""", 0, False
