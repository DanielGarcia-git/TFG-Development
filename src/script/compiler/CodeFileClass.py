from io import TextIOWrapper

class CodeFile:
    """_summary_
    """
    
    def __init__(self) -> None:
        """_summary_
        """

        self.__codeFile = TextIOWrapper
        self.__pathToFile = ""

    def setPathToFile(self, newPath: str) -> None:
        """_summary_

        Args:
            newPath (str): _description_
        """

        self.__pathToFile = newPath
        self.__codeFile = open(self.__pathToFile, 'r')

    def getData(self) -> list[str]:
        """_summary_

        Returns:
            list[str]: _description_
        """

        return self.__codeFile.readlines()