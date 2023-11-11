import os

class FileManager:
    """_summary_
    """
    
    @classmethod
    def createDirectory(self, directoryPath: str) -> None:
        """_summary_

        Args:
            directoryPath (str): _description_
        """

        if not os.path.exists(directoryPath):
            os.makedirs(directoryPath)