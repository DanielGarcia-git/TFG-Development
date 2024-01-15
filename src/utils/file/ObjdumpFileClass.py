from utils.file.FileClass import File
import re

class ObjdumpFile(File):
    """Represents an objdump file.

    This class provides methods to clean the objdump file and retrieve its content.

    Attributes:
        pathToFile (str): The path to the objdump file.
    """

    def __clean_objdump(self, file_path):
        """Cleans the objdump file by removing unnecessary lines.

        Args:
            file_path (str): The path to the objdump file.
        """

        with open(file_path, 'r') as file:
            lines = file.readlines()

        cleaned_lines = []
        inside_function = False
        for line in lines:
            if "Disassembly of section" in line:
                inside_function = False

            # Check if the line marks the start of a function
            if re.match(r"\d{16} \<.*\>:", line):
                inside_function = True

            if inside_function:
                cleaned_lines.append(line)

        with open(file_path, 'w') as file:
            file.writelines(cleaned_lines)
    
    def clean(self):
        """Cleans the objdump file."""

        self.__clean_objdump(self.pathToFile)
    
    def __str__(self) -> str:
        """Returns the content of the objdump file as a string.

        Returns:
            str: The content of the objdump file.
        """

        with open(self.pathToFile, 'r', encoding=self.getEncoding()) as file:
            content = ""
            for line in file:
                content += line
        return content