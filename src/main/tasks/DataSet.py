import os
import shutil
from main.tasks.Default import DefaultTask
from script.dataset.DataSetClass import DataSet
from script.dataset.DataFineTuningClass import DataFineTuning
from utils.enum.PathsEnum import Paths
from utils.file.CodeFileClass import CodeFile

class DataSetTask(DefaultTask):

    def __init__(self):
        """_summary_
        """

        super().__init__()
        self.__dataSet = DataSet()
        self.__asemblerFiles = list()
        self.__codeFiles = list()
    
    def getFileByPathAndType(self, path: str, type: str) -> None:
        """_summary_
        """

        codeFiles = []

        if shutil.os.path.exists(path) and os.listdir(path):
            # Recorrer directorio de repositorios y obtener los archivos de código en C
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(type):
                        codeFiles.append(CodeFile(str(os.path.join(root, file))))
        
        return codeFiles

    def defineTask(self) -> None:
        """_summary_
        """

        self.__asemblerFiles = self.getFileByPathAndType(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value, ".asm")
        self.__codeFiles = self.getFileByPathAndType(Paths.ROOT_PATH_LOCAL_REPOSITORIES.value, ".c")

        if self.__asemblerFiles:
            if self.__codeFiles:
                for codeFile in self.__codeFiles:
                    for asemblerFile in self.__asemblerFiles:
                        if codeFile.getFileName() == asemblerFile.getFileName():
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
        

