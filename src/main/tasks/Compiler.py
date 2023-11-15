import shutil
from main.tasks.Default import DefaultTask
from script.compiler.CompilerClass import Compiler
from utils.enum.PathsEnum import Paths
from script.compiler.CompilerOptionsClass import CompilerOptions
from script.compiler.CodeFileClass import CodeFile
import os

class CompilerTask(DefaultTask):

    def __init__(self):
        """_summary_
        """

        super().__init__()
        self.__compiler = Compiler()
        self.__compilerOptions = CompilerOptions()
        self.__codeFiles = []

    def __init__(self, arg_command=""):
        """_summary_

        Args:
            arg_command (str): _description_
        """

        super().__init__(arg_command)
        self.__compiler = Compiler()
        self.__compilerOptions = self.getCompilerOptions()
        self.__codeFiles = []

    def getCompilerOptions(self) -> CompilerOptions:
        """_summary_

        Returns:
            CompilerOptions: _description_
        """

        print(self.arg_command)

    def getCodeFiles(self) -> None:
        """_summary_

        Returns:
            list: _description_
        """
        
        self.__codeFiles = []

        if shutil.os.path.exists(str(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value)) and os.listdir(str(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value)):
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

        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value))
        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value))
        if not shutil.os.path.exists(str(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value)):
            os.makedirs(str(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value))

    def defineTask(self) -> None:
        """_summary_
        """

        self.getCodeFiles()
        self.generateDirectory()
        self.__compiler.setCodeFiles(self.__codeFiles)
        self.__compiler.setCompilerOptions(self.__compilerOptions)
        self.__compiler.compilerExec()