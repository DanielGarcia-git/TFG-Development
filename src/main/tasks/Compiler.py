import shutil
from main.tasks.Default import DefaultTask
from script.compiler.CompilerClass import Compiler
from main.log.LogManagerClass import LogManager
from utils.enum.PathsEnum import Paths
import os

class CompilerTask(DefaultTask):

    def __init__(self):
        """_summary_
        """

        super().__init__()
        self.__compiler = Compiler()
        self.__logManager = LogManager()
        self.__codeFiles = []

    def getCodeFiles(self) -> None:
        """_summary_

        Returns:
            list: _description_
        """
        
        self.__codeFiles = []

        if shutil.os.path.exists(str(Paths.ROOT_PATH_LOCAL_REPOSITORIES.value)) and os.listdir(str(Paths.ROOT_PATH_LOCAL_REPOSITORIES.value)):
            # Recorrer directorio de repositorios y obtener los archivos de código en C
            for root, dirs, files in os.walk(str(Paths.ROOT_PATH_LOCAL_REPOSITORIES.value)):
                for file in files:
                    if file.endswith(".c"):
                        self.__codeFiles.append(os.path.join(root, file))
        else:
            self.__logManager.logError("El directorio de repositorios está vacio o no existe")
            exit(1)

    def run(self) -> None:
        """_summary_
        """

        self.getCodeFiles()
        self.__compiler.setCodeFiles(self.__codeFiles)