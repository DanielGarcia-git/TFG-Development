from enum import Enum

class Arguments(Enum):
    """_summary_
    """

    REPOSITORY_SETUP = ("-r", "--repository-setup", "Descarga los repositorios especificados en el fichero de repositorios.txt")
    VERSION = ("-v", "--version", "Muestra la versión del programa")
    HELP = ("-h", "--help", "Muestra este mensaje de ayuda")

    def __init__(self, arg_short: str, arg_large: str, description: str) -> None:
        """_summary_

        Args:
            arg_short (str): _description_
            arg_large (str): _description_
            description (str): _description_
        """

        self.__arg_short = arg_short
        self.__arg_large = arg_large
        self.__description = description

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
    
        return f"{self.__arg_short}/{self.__arg_large} - {self.__description}"
    
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