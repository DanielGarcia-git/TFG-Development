import json
import os
import subprocess
import platform

from main.log.LogManagerClass import LogManager
from utils.file.CodeFileClass import CodeFile
from script.compiler.CompilerOptionsClass import CompilerOptions
from utils.enum.CompilersEnum import Compilers
from utils.enum.CompilerOptionsLevelEnum import CompilerOptionsLevel
from utils.enum.OperatingSystemEnum import OperatingSystem
from utils.enum.PathsEnum import Paths
from utils.file.FileClass import File
from utils.file.ObjdumpFileClass import ObjdumpFile

class Compiler:
    """A singleton class representing a compiler.

    This class provides functionality to compile code files using different compiler options
    based on the operating system. It also generates objdump files for the compiled executables.

    Attributes:
        __instance (Compiler): The singleton instance of the Compiler class.
        __logManager (LogManager): The log manager instance.
        __compilerOptions (list[CompilerOptions]): The list of available compiler options.
        __compilerOptionLevel (CompilerOptionsLevel): The current level of compiler options.
        __actualCompilerOption (CompilerOptions): The actual compiler option based on the level.
        __codeFiles (list[CodeFile]): The list of code files to be compiled.
        __operatingSystem (OperatingSystem): The operating system on which the compiler is running.
        __compilerExec (Compilers): The compiler executable.

    Methods:
        __new__(self): Creates a new instance of the Compiler class.
        __setPathToCompiler(self): Sets the path to the compiler executable based on the operating system.
        __setCompilerOptions(self): Sets the compiler options based on the operating system.
        __setOperatingSystem(self): Sets the operating system based on the platform.
        __createCommand(self, codeFile): Creates the compilation command for a code file.
        __compile(self, fileToCompile): Compiles a code file using the specified compiler options.
        getOperatingSystem(self): Returns the operating system.
        getCompilerOptionsLevel(self): Returns the current level of compiler options.
        getCompilerOptions(self): Returns the available compiler options.
        setCodeFiles(self, codeFiles): Sets the code files to be compiled.
        setJSONToCompilerOptions(self, pathToJSON): Sets the compiler options from a JSON file.
        setLevelCompilerOptions(self, compilerLevel): Sets the level of compiler options.
        compilerExec(self): Executes the compilation process.
    """

    __instance = None

    def __new__(self):
        """Creates a new instance of the Compiler class.

        Returns:
            Compiler: The newly created instance of the Compiler class.
        """

        if not self.__instance:
            self.__instance = super(Compiler, self).__new__(self)
            self.__logManager = LogManager()
            self.__compilerOptions = []
            self.__compilerOptionLevel = CompilerOptionsLevel.NONE
            self.__actualCompilerOption = CompilerOptions()
            self.__codeFiles = []
            self.__setOperatingSystem(self)
            self.__setPathToCompiler(self)
            self.__setCompilerOptions(self)
        return self.__instance

    def __setPathToCompiler(self) -> None:
        """Set the path to the compiler based on the operating system.

        This method determines the appropriate compiler executable based on the operating system.
        If the operating system is Windows, the Visual Studio compiler is used.
        If the operating system is Linux, the GCC compiler is used.
        If the operating system is neither Windows nor Linux, no compiler is set.
        """

        if self.__operatingSystem == OperatingSystem.WINDOWS:
            self.__compilerExec = Compilers.VISUAL_STUDIO
        elif self.__operatingSystem == OperatingSystem.LINUX:
            self.__compilerExec = Compilers.GCC
        else:
            self.__compilerExec = Compilers.NONE
    
    def __setCompilerOptions(self) -> None:
        """Set the compiler options based on the operating system.

        Reads the compiler options from a JSON file and populates the __compilerOptions list
        based on the current operating system.
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
        """Set the operating system based on the current platform.

        This method determines the operating system and sets the appropriate value
        for the `__operatingSystem` attribute.
        """

        if platform.system() == "Windows":
            self.__operatingSystem = OperatingSystem.WINDOWS
        elif platform.system() == "Linux":
            self.__operatingSystem = OperatingSystem.LINUX
        else:
            self.__operatingSystem = OperatingSystem.NONE
    
    def __createCommand(self, codeFile: CodeFile) -> list[str]:
        """Create the command for compiling the code file.

        Args:
            codeFile (CodeFile): The code file to be compiled.

        Returns:
            list[str]: The command for compiling the code file.
        """

        if self.__compilerOptionLevel == CompilerOptionsLevel.NONE:
            raise Exception("No se ha definido el nivel de opciones de compilación")

        if self.__operatingSystem == OperatingSystem.WINDOWS:
            option_fe = f"{os.path.join(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value, codeFile.getFileName())}.exe"
            option_fa = f"{os.path.join(Paths.PATH_TO_COMPILER_ASM_OUTPUT.value, codeFile.getFileName())}.asm"
            option_fo = f"{os.path.join(Paths.PATH_TO_COMPILER_OBJ_OUTPUT.value, codeFile.getFileName())}.obj"
            return [str(self.__compilerExec.value), codeFile.getPathToFile()] + self.__actualCompilerOption.getOptions() + [f"/Fe{option_fe}", f"/Fa{option_fa}", f"/Fo{option_fo}"]
        elif self.__operatingSystem == OperatingSystem.LINUX:
            return [str(self.__compilerExec.value)] + self.__actualCompilerOption.getOptions() + [codeFile.getPathToFile(), "-o", os.path.join(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value, codeFile.getFileName())]
        else:
            return None

    def __compile(self, fileToCompile: CodeFile) -> bool:
        """Compiles the given code file.

        Args:
            fileToCompile (CodeFile): The code file to compile.

        Returns:
            bool: True if the compilation is successful, False otherwise.
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
        """Returns the operating system associated with the compiler.

        Returns:
            OperatingSystem: The operating system associated with the compiler.
        """

        return self.__operatingSystem
    
    def getCompilerOptionsLevel(self) -> CompilerOptionsLevel:
        """Returns the compiler options level.

        Returns:
            CompilerOptionsLevel: The compiler options level.
        """

        return self.__compilerOptionLevel
    
    def getCompilerOptions(self) -> CompilerOptions:
        """Get the compiler options.

        Returns:
            CompilerOptions: The compiler options.
        """

        return self.__compilerOptions
    
    def setCodeFiles(self, codeFiles: list[CodeFile]) -> None:
        """
        Set the code files for the compiler.

        Args:
            codeFiles (list[CodeFile]): A list of CodeFile objects representing the code files to be set.
        """

        self.__codeFiles = codeFiles

    def setJSONToCompilerOptions(self, pathToJSON: str) -> None:
        """Set the compiler options from a JSON file.

        Args:
            pathToJSON (str): The path to the JSON file containing the compiler options.
        """

        jsonFile = open(pathToJSON, "r")
        jsonObject = json.load(jsonFile)

        for compilerOption in jsonObject["compilerOptions"]:
            options = []
            if self.__operatingSystem == OperatingSystem.WINDOWS:
                options = compilerOption["options"]["windows"]
            elif self.__operatingSystem == OperatingSystem.LINUX:
                options = compilerOption["options"]["linux"]

            self.__compilerOptions.append(CompilerOptions(compilerOption["id"], options))
    
    def setLevelCompilerOptions(self, compilerLevel: CompilerOptionsLevel) -> None:
        """Set the level of compiler options.

        Args:
            compilerLevel (CompilerOptionsLevel): The level of compiler options to set.
        """
        
        self.__compilerOptionLevel = compilerLevel
        for option in self.__compilerOptions:
            if option.getId() == compilerLevel.value:
                self.__logManager.logDebug(f"Se ha definido el nivel de opciones de compilación a {compilerLevel.value}")
                self.__actualCompilerOption = option
                break
    
    def compilerExec(self) -> None:
        """Executes the compilation process.

        This method checks the compiler options, code files, and compiler executable.
        It then compiles each code file and generates objdump files for the compiled executables.
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

        exeFiles = []

        # Ponemos en exeFiles el path a todos los archivos .exe que encontramos en la carpeta Paths.PATH_TO_COMPILER_EXE_OUTPUT
        for root, dirs, files in os.walk(str(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value)):
            for file in files:
                if file.endswith(".exe") and self.__operatingSystem == OperatingSystem.WINDOWS:
                    exeFiles.append(os.path.join(root, file))
                elif self.__operatingSystem == OperatingSystem.LINUX:
                    exeFiles.append(os.path.join(root, file))
        
        # Generamos los archivos .objdump con formato de .txt
        self.__logManager.log("Generando archivos .objdump")
        for exe in exeFiles:
            exeFile = File(exe)
            self.__logManager.log(f"Generando archivo .objdump para {exeFile.getFileName()}")
            objdump_command = []
            if self.__operatingSystem == OperatingSystem.WINDOWS:
                objdump_command = ["dumpbin", "/DISASM", os.path.join(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value, exeFile.getFileName()) + ".exe"]
            elif self.__operatingSystem == OperatingSystem.LINUX:
                objdump_command = ["objdump", "-d", os.path.join(Paths.PATH_TO_COMPILER_EXE_OUTPUT.value, exeFile.getFileName())]

            self.__logManager.logDebug(f"Comando de objdump: {objdump_command}")
            with open(os.path.join(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value, f"{exeFile.getFileName()}.txt"), "w") as f:
                subprocess.run(objdump_command, stdout=f)

        for root, dirs, files in os.walk(str(Paths.PATH_TO_COMPILER_OBJDUMP_OUTPUT.value)):
            for file in files:
                objdumpFile = ObjdumpFile(os.path.join(root, file))
                objdumpFile.clean()
    