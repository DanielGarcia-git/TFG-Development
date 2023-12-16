import os
import shutil

from utils.abstract.Default import DefaultTask
from utils.file.CodeFileClass import CodeFile
from script.compiler.CompilerClass import Compiler
from utils.enum.CompilerOptionsLevelEnum import CompilerOptionsLevel
from utils.enum.PathsEnum import Paths

class CompilerTask(DefaultTask):
    """_summary_
    """

    def __init__(self, arg_command: str = ""):
        """_summary_

        Args:
            arg_command (str, optional): _description_. Defaults to "".
        """

        super().__init__(arg_command)
        self.__compiler = Compiler()
        self.__compiler.setJSONToCompilerOptions(self.arg_command)
        self.__codeFiles = []

    def getCodeFiles(self) -> None:
        """_summary_
        """
        
        self.__codeFiles = []
        if shutil.os.path.exists(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value) and os.listdir(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value):
            for root, dirs, files in os.walk(str(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value)):
                for file in files:
                    if file.endswith(".c"):
                        self.__codeFiles.append(CodeFile(str(os.path.join(root, file))))
        else:
            self.logManager.logError("El directorio de repositorios está vacio o no existe")
            exit(1)
    
    def generateDirectory(self) -> None:
        """_summary_
        """

        if not shutil.os.path.exists(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value):
            os.makedirs(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value)
        if not shutil.os.path.exists(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value):
            os.makedirs(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value)
        if not shutil.os.path.exists(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value):
            os.makedirs(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value)
        if not shutil.os.path.exists(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value):
            os.makedirs(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value)

    def defineTask(self) -> None:
        """_summary_
        """

        self.getCodeFiles()
        self.generateDirectory()
        self.__compiler.setCodeFiles(self.__codeFiles)
        self.__compiler.setLevelCompilerOptions(CompilerOptionsLevel.LEVEL_1)
        self.logManager.logDebug(f"Se ha definido el nivel de opciones de compilación a {self.__compiler.getCompilerOptionsLevel()}")
        self.__compiler.compilerExec()