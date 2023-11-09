from io import TextIOWrapper
import os
import chardet
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
        self.__codeFile = open(self.__pathToFile, encoding=None)

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

        self.__codeFile = open(self.__pathToFile, encoding=None)
        return self.__codeFile.readlines()
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        with open(self.__pathToFile, 'rb') as file:
            detector = chardet.universaldetector.UniversalDetector()
            for line in file:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()

        encoding = detector.result['encoding']

        with open(self.__pathToFile, 'r', encoding=encoding) as file:
            content = ""
            for line in file:
                content += line
        return content