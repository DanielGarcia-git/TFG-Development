from utils.file.FileClass import File
import chardet
from pathlib import Path

class CodeFile(File):
    """_summary_
    """
    
    def __init__(self) -> None:
        """_summary_
        """

        super().__init__()
    
    def __init__(self, path: str) -> None:
        """_summary_
        """

        super().__init__(path)
    
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