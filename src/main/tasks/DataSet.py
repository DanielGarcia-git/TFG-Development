import os
import shutil

from utils.abstract.Default import DefaultTask
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
        self.__asemblerFiles = list[CodeFile]
        self.__codeFiles = list[CodeFile]
    
    def getFileByPathAndType(self, path: str, type: str) -> None:
        """_summary_
        """

        codeFiles = []

        if shutil.os.path.exists(path) and os.listdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(type):
                        codeFiles.append(CodeFile(str(os.path.join(root, file))))
        
        return codeFiles

    def defineTask(self) -> None:
        """_summary_
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
        

