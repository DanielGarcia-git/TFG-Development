from io import TextIOWrapper
from pathlib import Path
import chardet

class File:
    """A class representing a file.

    Attributes:
        file (TextIOWrapper): The file object.
        pathToFile (str): The path to the file.
    """

    def __init__(self, path: str = "") -> None:
        """Initialize a File object.

        Args:
            path (str, optional): The path to the file. Defaults to "".
        """

        self.file = TextIOWrapper
        self.pathToFile = path
    
    def setPathToFile(self, newPath: str) -> None:
        """Set the path to the file.

        Args:
            newPath (str): The new path to the file.
        """

        self.pathToFile = newPath
    
    def getPathToFile(self) -> str:
        """Get the path to the file.

        Returns:
            str: The path to the file.
        """

        return self.pathToFile

    def getFileName(self) -> str:
        """Get the name of the file.

        Returns:
            str: The name of the file.
        """

        return Path(self.pathToFile).stem
    
    def getData(self) -> list[str]:
        """Get the data from the file.

        Returns:
            list[str]: The data from the file as a list of strings.
        """

        self.file = open(self.pathToFile, encoding=None)
        return self.file.readlines()
    
    def getEncoding(self) -> str:
        """Get the encoding of the file.

        Returns:
            str: The encoding of the file.
        """

        with open(self.pathToFile, 'rb') as file:
            detector = chardet.universaldetector.UniversalDetector()
            for line in file:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
        
        return detector.result['encoding']
    
