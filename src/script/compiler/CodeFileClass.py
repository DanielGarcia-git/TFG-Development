from io import TextIOWrapper
import os
from pathlib import Path

class CodeFile:
    """_summary_
    """
    
    def __init__(self) -> None:
        """_summary_
        """

        self.__codeFile = TextIOWrapper
        self.__pathToFile = ""
    
    def __init__(self, path: str) -> None:
        """_summary_
        """

        self.__codeFile = TextIOWrapper
        self.__pathToFile = path

    def setPathToFile(self, newPath: str) -> None:
        """_summary_

        Args:
            newPath (str): _description_
        """

        self.__pathToFile = newPath
        self.__codeFile = open(self.__pathToFile, 'r')

    def getPathToFile(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self.__pathToFile
    
    def getFileName(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return Path(self.__pathToFile).stem

    def getData(self) -> list[str]:
        """_summary_

        Returns:
            list[str]: _description_
        """

        return self.__codeFile.readlines()