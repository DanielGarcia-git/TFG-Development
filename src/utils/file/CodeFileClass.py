from utils.file.FileClass import File

class CodeFile(File):
    """Represents a code file.

    This class inherits from the File class and provides additional functionality specific to code files.

    Attributes:
        pathToFile (str): The path to the code file.
    """
    
    def __str__(self) -> str:
        """Returns the content of the code file as a string.

        Returns:
            str: The content of the code file.
        """

        with open(self.pathToFile, 'r', encoding=self.getEncoding()) as file:
            content = ""
            for line in file:
                content += line
        return content