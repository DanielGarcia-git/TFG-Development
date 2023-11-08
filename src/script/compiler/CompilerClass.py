from script.compiler.CompilerOptionsClass import CompilerOptions
from script.compiler.CodeFileClass import CodeFile
from utils.enum.CompilersEnum import Compilers
from utils.enum.OperatingSystemEnum import OperatingSystem

import platform

class Compiler:
    """_summary_
    """

    __instance = None

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.__instance = super(Compiler, self).__new__(self)
            self.__compilerOptions = None
            self.__setOperatingSystem(self)
            self.__setPathToCompiler(self)
            self.__codeFiles = []
        return self.__instance

    def __setPathToCompiler(self) -> None:
        """_summary_
        """

        if self.__operatingSystem == OperatingSystem.WINDOWS:
            self.__compilerExec = Compilers.VISUAL_STUDIO
        elif self.__operatingSystem == OperatingSystem.LINUX:
            self.__compilerExec = Compilers.GCC
        else:
            self.__compilerExec = Compilers.NONE
    
    def __setOperatingSystem(self) -> None:
        """_summary_
        """

        if platform.system() == "Windows":
            self.__operatingSystem = OperatingSystem.WINDOWS
        elif platform.system() == "Linux":
            self.__operatingSystem = OperatingSystem.LINUX
        else:
            self.__operatingSystem = OperatingSystem.NONE

    def __compile(self, fileToCompile: CodeFile) -> None:
        """_summary_

        Args:
            fileToCompile (CodeFile): _description_
        """

        pass
    
    def getOperatingSystem(self) -> OperatingSystem:
        """_summary_

        Returns:
            OperatingSystem: _description_
        """

        return self.__operatingSystem
    
    def getCompilerOptions(self) -> CompilerOptions:
        """_summary_

        Returns:
            CompilerOptions: _description_
        """

        return self.__compilerOptions
    
    def setCodeFiles(self, codeFiles: list[CodeFile]) -> None:
        """_summary_

        Args:
            codeFiles (list[CodeFile]): _description_
        """

        self.__codeFiles = codeFiles
    
    def compilerExec(self) -> None:
        """_summary_
        """

        if self.__compilerOptions == None and self.__codeFiles.count() == 0:
            pass
        else:
            for codeFile in self.__codeFiles:
                self.__compile(codeFile)
