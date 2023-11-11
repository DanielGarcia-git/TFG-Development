import shutil
from main.tasks.Default import DefaultTask
from script.compiler.CompilerClass import Compiler
from utils.enum.PathsEnum import Paths
from script.compiler.CompilerOptionsClass import CompilerOptions
from utils.file.CodeFileClass import CodeFile
import os

class CompilerTask(DefaultTask):

    def __init__(self):
        """_summary_
        """

        super().__init__()
        self.__compiler = Compiler()
        self.__compilerOptions = CompilerOptions()
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
                        self.__codeFiles.append(CodeFile(str(os.path.join(root, file))))
        else:
            self.logManager.logError("El directorio de repositorios está vacio o no existe")
            exit(1)
    
    def generateDirectory(self) -> None:
        """_summary_
        """

        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value))
        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value))
        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value))
        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value))

    def defineTask(self) -> None:
        """_summary_
        """

        self.getCodeFiles()
        self.generateDirectory()
        self.__compiler.setCodeFiles(self.__codeFiles)
        self.__compiler.setCompilerOptions(self.__compilerOptions)
        self.__compiler.compilerExec()