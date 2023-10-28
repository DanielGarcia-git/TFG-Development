import string
from script.compiler.CompilerOptionsClass import CompilerOptions
from script.compiler.CodeFileClass import CodeFile
from utils.enum.CompilersEnum import Compilers
from utils.enum.OperatingSystemEnum import OperatingSystem

import platform

class Compiler:
    '''
    '''

    def __init__(self) -> None:
        self.__compilerOptions = CompilerOptions()
        self.__operatingSystem = OperatingSystem.NONE
        self.__codeFiles = []
        self.__compilerExec = Compilers.NONE

    def __setPathToCompiler(self) -> None:
        if self.__operatingSystem == OperatingSystem.WINDOWS:
            self.__compilerExec = Compilers.VISUAL_STUDIO
        elif self.__operatingSystem == OperatingSystem.LINUX:
            self.__compilerExec = Compilers.GCC
        else:
            self.__compilerExec = Compilers.NONE
    
    def __setOperatingSystem(self) -> None:
        if platform.system() == "Windows":
            self.__operatingSystem = OperatingSystem.WINDOWS
        elif platform.system() == "Linux":
            self.__operatingSystem = OperatingSystem.LINUX
        else:
            self.__operatingSystem = OperatingSystem.NONE
    
    def getOperatingSystem(self) -> OperatingSystem:
        return self.__operatingSystem
    
    def getCompilerOptions(self) -> CompilerOptions:
        return self.__compilerOptions
