import shutil

from utils.abstract.Default import DefaultTask
from utils.enum.PathsEnum import Paths

class CleanUpTask(DefaultTask):
    """This class implements the task that cleans all the temporary files
    """

    def clean(self) -> None:
        """This function cleans all the temporary files
        """

        self.logManager.log(f"Eliminando carpeta output: {str(Paths.PATH_TO_OUTPUT.value)}")
        try:
            shutil.rmtree(str(Paths.PATH_TO_OUTPUT.value))
            shutil.rmtree(str(Paths.PATH_TO_LOG_DIR.value))
        except OSError as e:
            self.logManager.logError(f"Error: {str(e)} - {str(Paths.PATH_TO_OUTPUT.value)}")

    def defineTask(self) -> None:
        """This function defines the behaivor of the task, in this case
           cleans all the temporary files
        """

        self.clean()