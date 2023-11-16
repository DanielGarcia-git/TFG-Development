import shutil

from main.tasks.Default import DefaultTask
from utils.enum.PathsEnum import Paths

class CleanUpTask(DefaultTask):

    # Crea una funcion para eliminar la carpeta output
    def clean(self) -> None:
        """_summary_
        """

        self.logManager.log(f"Eliminando carpeta output: {str(Paths.PATH_TO_OUTPUT.value)}")
        try:
            shutil.rmtree(str(Paths.PATH_TO_OUTPUT.value))
        except OSError as e:
            self.logManager.logError(f"Error: {str(e)} - {str(Paths.PATH_TO_OUTPUT.value)}")

    def defineTask(self) -> None:
        """_summary_
        """

        self.clean()