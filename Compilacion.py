import os
import subprocess
import platform
import shutil
from setup import setupRepository

def compile_c_to_asm(root_dir):
    # Obtener el sistema operativo actual
    operating_system = platform.system()

    #setup.setupRepository()

    # Encontrar todos los archivos con extensión .c en el directorio raíz
    c_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".c"):
                c_files.append(os.path.join(root, file))

    # Crear la carpeta "output" dentro del directorio raíz
    output_dir = os.path.join(root_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Compilar cada archivo C encontrado y generar el código ensamblador
    for c_file in c_files:
        # Obtener el nombre del archivo sin la extensión .c y reemplazar espacios por guiones bajos
        file_name = os.path.splitext(os.path.basename(c_file))[0].replace(" ", "_")

        # Comando de compilación según el sistema operativo
        if operating_system == "Windows":
            compile_command = f"cl {c_file} /Fa{os.path.join(output_dir, file_name)}.asm"
        else:  # Linux
            compile_command = f"gcc -S {c_file} -o {os.path.join(output_dir, file_name)}.s"

        # Ejecutar el comando de compilación
        subprocess.run(compile_command, shell=True)

        print(f"Compilado {c_file} -> {os.path.join(output_dir, file_name)}.asm")

# Directorio raíz donde se buscarán los programas en C
root_directory = ".\Codigos_C"

setupRepository()

# Llamar a la función para compilar los archivos C y generar el código ensamblador
compile_c_to_asm(root_directory)
