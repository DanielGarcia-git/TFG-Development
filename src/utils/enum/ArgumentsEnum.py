from enum import Enum

class Arguments(Enum):
    """An enumeration class representing command line arguments.

    Each argument is defined with a short and long option, a description, and whether it requires an argument or not.

    Attributes:
        REPOSITORY_SETUP (tuple): A tuple representing the repository setup argument.
        COMPILER_SETUP (tuple): A tuple representing the compiler setup argument.
        DATASET_SETUP (tuple): A tuple representing the dataset setup argument.
        CLEAN_UP (tuple): A tuple representing the clean up argument.
        DEBUG (tuple): A tuple representing the debug argument.
        VERSION (tuple): A tuple representing the version argument.
        HELP (tuple): A tuple representing the help argument.
    """

    REPOSITORY_SETUP = ("-r", "--repository-setup", "Descarga los repositorios especificados en el fichero de repositorios.txt", False)
    COMPILER_SETUP = ("-c", "--compiler-setup", "Compila todos los archivos .c que se encuentren en el directorio de repositorios", True)
    DATASET_SETUP = ("-d", "--dataset-setup", "Genera el dataset a partir de los archivos .asm generados por el compilador", False)
    CLEAN_UP = ("-cl", "--clean-up", "Elimina todos los archivos generados por el programa", False)
    DEBUG = ("-D", "--debug", "Muestra mensajes de debug", False)
    VERSION = ("-v", "--version", "Muestra la versión del programa", False)
    HELP = ("-h", "--help", "Muestra este mensaje de ayuda", False)

    def __init__(self, arg_short: str, arg_large: str, description: str, has_arg: bool) -> None:
        """Initialize the Arguments enum.

        Args:
            arg_short (str): The short option of the argument.
            arg_large (str): The long option of the argument.
            description (str): The description of the argument.
            has_arg (bool): Whether the argument requires an argument or not.
        """

        self.__arg_short = arg_short
        self.__arg_large = arg_large
        self.__has_arg = has_arg
        self.__description = description

    def __str__(self) -> str:
        """Return a string representation of the argument.

        Returns:
            str: The string representation of the argument.
        """

        options = ""
        if self.__has_arg:
            options = " <arg>"
        return f"{self.__arg_short}/{self.__arg_large}{options} - {self.__description}"
    
    def getArgShort(self) -> str:
        """Get the short option of the argument.

        Returns:
            str: The short option of the argument.
        """
    
        return self.__arg_short
    
    def getArgLarge(self) -> str:
        """Get the long option of the argument.

        Returns:
            str: The long option of the argument.
        """
    
        return self.__arg_large
    
    def getHasArg(self) -> bool:
        """Check if the argument requires an argument.

        Returns:
            bool: True if the argument requires an argument, False otherwise.
        """

        return self.__has_arg