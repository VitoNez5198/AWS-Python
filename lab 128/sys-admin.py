import os
import subprocess
import sys

# Ejercicio 1: Uso de os.system
print("--- Ejercicio 1: os.system ---")
os.system("ls")

# Ejercicio 2, 3 y 4: Uso de subprocess.run
print("\n--- Ejercicio 4: subprocess.run con tres argumentos ---")
subprocess.run(["ls", "-l", "README.md"])

# Ejercicio 5: Recuperación de información del sistema
print("\n--- Ejercicio 5: uname -a ---")
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])


# Tarea 6: Recuperación de información sobre el espacio en disco (Windows vs Linux)
print("\n--- Tarea 6: Recuperación de información sobre el espacio en disco ---")

if sys.platform.startswith("win"):
    # En Windows, usamos PowerShell para obtener la información de volumen estructurada
    command = "powershell"
    commandArgument = "-Command \"Get-Volume | Select-Object @{Name='Unidad'; Expression={$_.DriveLetter}}, @{Name='Formato'; Expression={$_.FileSystem}}, @{Name='GB Total'; Expression={[math]::round($_.Size/1GB, 2)}}, @{Name='GB Libres'; Expression={[math]::round($_.SizeRemaining/1GB, 2)}}\""
    
    print(f'Gathering disk space information with command: {command}')
    resultado = subprocess.run(f"{command} {commandArgument}", shell=True, capture_output=True, text=True)
    print(resultado.stdout)
else:
    # En Linux, usamos el comando 'df' como se menciona en el laboratorio original
    command = "df"
    commandArgument = "-h"
    print(f'Gathering disk space information with command: {command} {commandArgument}')
    subprocess.run([command, commandArgument])

