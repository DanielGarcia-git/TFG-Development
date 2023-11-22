from io import TextIOWrapper
from pathlib import Path
import chardet

class File:
    """_summary_
    """

    def __init__(self, path: str = "") -> None:
        """_summary_
        """

        self.file = TextIOWrapper
        self.pathToFile = path
    
    def setPathToFile(self, newPath: str) -> None:
        """_summary_

        Args:
            newPath (str): _description_
        """

        self.pathToFile = newPath
    
    def getPathToFile(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self.pathToFile

    def getFileName(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return Path(self.pathToFile).stem
    
    def getData(self) -> list[str]:
        """_summary_

        Returns:
            list[str]: _description_
        """

        self.file = open(self.pathToFile, encoding=None)
        return self.file.readlines()
    
    def getEncoding(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        with open(self.pathToFile, 'rb') as file:
            detector = chardet.universaldetector.UniversalDetector()
            for line in file:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
        
        return detector.result['encoding']
    
