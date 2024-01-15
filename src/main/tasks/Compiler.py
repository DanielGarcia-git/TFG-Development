import os
import shutil

from utils.abstract.Default import DefaultTask
from utils.file.CodeFileClass import CodeFile
from script.compiler.CompilerClass import Compiler
from utils.enum.CompilerOptionsLevelEnum import CompilerOptionsLevel
from utils.enum.PathsEnum import Paths

class CompilerTask(DefaultTask):
    """Represents a task for compiling code files.

    This class inherits from the DefaultTask class and provides methods for generating directories,
    defining the task, and executing the compiler.

    Attributes:
        __compiler (Compiler): The compiler object used for compilation.
        __codeFiles (list): A list of CodeFile objects representing the code files to be compiled.

    Args:
        arg_command (str, optional): The command to be passed to the compiler. Defaults to "".
    """

    def __init__(self, arg_command: str = ""):
        """Initializes a new instance of the CompilerTask class.

        Args:
            arg_command (str, optional): The command to be passed to the compiler. Defaults to "".
        """

        super().__init__(arg_command)
        self.__compiler = Compiler()
        self.__compiler.setJSONToCompilerOptions(self.arg_command)
        self.__codeFiles = []

    def getCodeFiles(self) -> None:
        """Gets the code files to be compiled.

        This method searches for code files in the local code repositories directory and adds them to the __codeFiles list.
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
        """Generates the required directories for compilation.

        This method creates the directories for the assembly output, object output, executable output, and objdump output
        if they do not already exist.
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
        """Defines the compilation task.

        This method calls the getCodeFiles() and generateDirectory() methods, sets the code files and compiler options,
        and executes the compiler.
        """

        self.getCodeFiles()
        self.generateDirectory()
        self.__compiler.setCodeFiles(self.__codeFiles)
        self.__compiler.setLevelCompilerOptions(CompilerOptionsLevel.LEVEL_1)
        self.logManager.logDebug(f"Se ha definido el nivel de opciones de compilación a {self.__compiler.getCompilerOptionsLevel()}")
        self.__compiler.compilerExec()