import os
import shutil

from utils.abstract.Default import DefaultTask
from script.dataset.DataSetClass import DataSet
from script.dataset.DataFineTuningClass import DataFineTuning
from utils.enum.PathsEnum import Paths
from utils.file.CodeFileClass import CodeFile

class DataSetTask(DefaultTask):
    """Represents a task for creating a dataset.

    This task collects data from assembler files and corresponding code files
    to build a dataset for further processing.

    Args:
        DefaultTask (type): The base class for tasks.

    Attributes:
        __dataSet (DataSet): The dataset object.
        __asemblerFiles (list[CodeFile]): The list of assembler files.
        __codeFiles (list[CodeFile]): The list of code files.
    """

    def __init__(self):
        """Initializes a new instance of the DataSetTask class.
        """

        super().__init__()
        self.__dataSet = DataSet()
        self.__asemblerFiles = list[CodeFile]
        self.__codeFiles = list[CodeFile]
    
    def getFileByPathAndType(self, path: str, type: str) -> None:
        """Returns a list of code files found in the specified path with the given file type.

        Args:
            path (str): The path to search for code files.
            type (str): The file type to filter the code files.

        Returns:
            list[CodeFile]: The list of code files found.
        """

        codeFiles = []

        if shutil.os.path.exists(path) and os.listdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(type):
                        codeFiles.append(CodeFile(str(os.path.join(root, file))))
        
        return codeFiles

    def defineTask(self) -> None:
        """Defines the task to build the dataset.
        """
        
        self.__asemblerFiles = self.getFileByPathAndType(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value, ".txt")
        self.__codeFiles = self.getFileByPathAndType(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value, ".c")

        if self.__asemblerFiles:
            if self.__codeFiles:
                self.logManager.log("Recopilando los datos para construir el dataset")
                for asemblerFile in self.__asemblerFiles:
                    for codeFile in self.__codeFiles:
                        if codeFile.getFileName() == asemblerFile.getFileName():
                            self.logManager.logDebug(f"Se ha encontrado el archivo {codeFile.getFileName()}")
                            dataFineTuning = DataFineTuning()
                            dataFineTuning.setOutput(str(codeFile))
                            dataFineTuning.setInput(str(asemblerFile))
                            self.__dataSet.addData(dataFineTuning)
                self.__dataSet.exportDataSet()
            else:
                self.logManager.logError("El directorio de repositorios está vacio o no existe")
                exit(1)
        else:
            self.logManager.logError("El directorio de codigo en ensamblado está vacio o no existe")
            exit(1)
