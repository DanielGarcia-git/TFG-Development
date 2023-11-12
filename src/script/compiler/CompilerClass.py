import json
import os
import subprocess
from script.compiler.CompilerOptionsClass import CompilerOptions
from script.compiler.CodeFileClass import CodeFile
from utils.enum.CompilersEnum import Compilers
from utils.enum.OperatingSystemEnum import OperatingSystem
from main.log.LogManagerClass import LogManager
from utils.enum.PathsEnum import Paths
from utils.enum.CompilerOptionsLevelEnum import CompilerOptionsLevel
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
            self.__logManager = LogManager()
            self.__compilerOptions = [CompilerOptions]
            self.__compilerOptionLevel = CompilerOptionsLevel.NONE
            self.__actualCompilerOption = CompilerOptions()
            self.__codeFiles = []
            self.__setOperatingSystem(self)
            self.__setPathToCompiler(self)
            self.__setCompilerOptions(self)
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
    
    def __setCompilerOptions(self) -> None:
        """_summary_
        """

        jsonFile = open(str(Paths.PATH_TO_COMPILER_OPTIONS.value), "r")
        jsonObject = json.load(jsonFile)

        for compilerOption in jsonObject["compilerOptions"]:
            options = []
            if self.__operatingSystem == OperatingSystem.WINDOWS:
                options = compilerOption["options"]["windows"]
            elif self.__operatingSystem == OperatingSystem.LINUX:
                options = compilerOption["options"]["linux"]

            self.__compilerOptions.append(CompilerOptions(compilerOption["id"], options))
    
    def __setOperatingSystem(self) -> None:
        """_summary_
        """

        if platform.system() == "Windows":
            self.__operatingSystem = OperatingSystem.WINDOWS
        elif platform.system() == "Linux":
            self.__operatingSystem = OperatingSystem.LINUX
        else:
            self.__operatingSystem = OperatingSystem.NONE
    
    def __createCommand(self, codeFile: CodeFile) -> str:
        """_summary_

        Args:
            codeFile (CodeFile): _description_

        Returns:
            str: _description_
        """

        option_fe = f"/Fe{os.path.join(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value, codeFile.getFileName())}.exe"
        option_fa = f"/Fa{os.path.join(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value, codeFile.getFileName())}.asm"
        option_fo = f"/Fo{os.path.join(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value, codeFile.getFileName())}.obj"

        if self.__compilerOptionLevel == CompilerOptionsLevel.NONE:
            raise Exception("No se ha definido el nivel de opciones de compilación")

        if self.__operatingSystem == OperatingSystem.WINDOWS:
            return f"{str(self.__compilerExec.value)} {codeFile.getPathToFile()} {self.__actualCompilerOption.getOptions()} {option_fa} {option_fe} {option_fo}"
        elif self.__operatingSystem == OperatingSystem.LINUX:
            return f""
        else:
            return None

    def __compile(self, fileToCompile: CodeFile) -> bool:
        """_summary_

        Args:
            fileToCompile (CodeFile): _description_
        """

        
        compile_command = self.__createCommand(fileToCompile)
        self.__logManager.log(f"Compilando {fileToCompile.getPathToFile()}")
        self.__logManager.logDebug(f"Comando de compilación: {compile_command}")
        result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            self.__logManager.logError("El comando falló con el código de salida: " + str(result.returncode))
            return False
        else:
            self.__logManager.log("El comando se ejecutó con éxito")
            return True
    
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
    
    def setLevelCompilerOptions(self, compilerLevel: CompilerOptionsLevel) -> None:
        """_summary_

        Args:
            compilerLevel (CompilerOptionsLevel): _description_
        """

        self.__compilerOptionLevel = compilerLevel
        for option in self.__compilerOptions:
            if option.getId() == compilerLevel.value:
                self.__actualCompilerOption = option
                break
    
    def compilerExec(self) -> None:
        """_summary_
        """

        if self.__compilerOptions == None:
            self.__logManager.logError("No se han definido las opciones de compilación")
            exit(1)
        elif len(self.__codeFiles) == 0:
            self.__logManager.logError("No se han definido archivos de código")
            exit(1)
        elif self.__compilerExec == Compilers.NONE:
            self.__logManager.logError("No se ha definido el compilador")
            exit(1)
        else:
            failCount = 0
            count = 0
            self.__logManager.log(f"Compilando {len(self.__codeFiles)} archivos")
            for codeFile in self.__codeFiles:
                count += 1
                self.__logManager.log(f"Compilando archivo {count} de {len(self.__codeFiles)}")
                if self.__compile(codeFile):
                    failCount += 1

            self.__logManager.log(f"Se compiló {len(self.__codeFiles) - failCount} de {len(self.__codeFiles)} archivos")
            
