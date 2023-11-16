from enum import Enum

class Arguments(Enum):
    """_summary_
    """

    REPOSITORY_SETUP = ("-r", "--repository-setup", "Descarga los repositorios especificados en el fichero de repositorios.txt")
    COMPILER_SETUP = ("-c", "--compiler-setup", "Compila todos los archivos .c que se encuentren en el directorio de repositorios")
    DATASET_SETUP = ("-d", "--dataset-setup", "Genera el dataset a partir de los archivos .asm generados por el compilador")
    DEBUG = ("-D", "--debug", "Muestra mensajes de debug")
    VERSION = ("-v", "--version", "Muestra la versión del programa")
    HELP = ("-h", "--help", "Muestra este mensaje de ayuda")

    def __init__(self, arg_short: str, arg_large: str, description: str, has_arg: bool) -> None:
        """_summary_

        Args:
            arg_short (str): _description_
            arg_large (str): _description_
            description (str): _description_
            has_arg (bool): _description_
        """

        self.__arg_short = arg_short
        self.__arg_large = arg_large
        self.__has_arg = has_arg
        self.__description = description

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        options = ""
        if self.__has_arg:
            options = " <arg>"
        return f"{self.__arg_short}/{self.__arg_large}{options} - {self.__description}"
    
    def getArgShort(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
    
        return self.__arg_short
    
    def getArgLarge(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
    
        return self.__arg_large
    
    def getHasArg(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """

        return self.__has_arg