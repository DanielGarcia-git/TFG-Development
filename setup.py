import os
from git import Repo

# Función para descargar un repositorio
def descargar_repositorio(repo_url, destino):
    try:
        repo = Repo.clone_from(repo_url, destino)
        print(f"Repositorio {repo_url} descargado en {destino}")
    except Exception as e:
        print(f"No se pudo descargar el repositorio {repo_url}")
        print(str(e))

def setupRepository():
    # Ruta del archivo con las direcciones a los repositorios
    archivo_repositorios = "repositorios.txt"

    # Subcarpeta donde se guardarán los repositorios descargados
    subcarpeta_destino = "Codigos_C"

    # Crear la subcarpeta de destino si no existe
    if not os.path.exists(subcarpeta_destino):
        os.makedirs(subcarpeta_destino)
    # Leer el archivo de repositorios y descargar cada uno
    with open(archivo_repositorios, "r") as file:
        for linea in file:
            linea = linea.strip()
            if linea:
                nombre_repositorio = linea.split("/")[-1].replace(".git", "")
                destino = os.path.join(subcarpeta_destino, nombre_repositorio)
                descargar_repositorio(linea, destino)