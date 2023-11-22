from utils.file.FileClass import File

class CodeFile(File):
    """_summary_
    """
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        with open(self.pathToFile, 'r', encoding=self.getEncoding()) as file:
            content = ""
            for line in file:
                content += line
        return content