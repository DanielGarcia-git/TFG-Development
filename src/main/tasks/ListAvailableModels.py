import subprocess
from main.tasks.Default import DefaultTask
from utils.enum.PathsEnum import Paths

class ListAvailableModelsTask(DefaultTask):

    def defineTask(self) -> None:

        command = f"python {Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES}\\lit-gpt\\scripts\\download.py"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("Listado de modelos disponibles:")
            print(result.stdout)