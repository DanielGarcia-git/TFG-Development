from utils.file.FileClass import File
import re

class ObjdumpFile(File):
    """_summary_
    """


    def __clean_objdump(self, file_path):
        """_summary_
        """

        with open(file_path, 'r') as file:
            lines = file.readlines()

        cleaned_lines = []
        inside_function = False
        for line in lines:
            if "Disassembly of section" in line:
                inside_function = False

            # Revisar si la línea marca el inicio de una función
            if re.match(r"\d{16} \<.*\>:", line):
                inside_function = True

            if inside_function:
                cleaned_lines.append(line)

        with open(file_path, 'w') as file:
            file.writelines(cleaned_lines)
    
    def clean(self):
        """_summary_
        """

        self.__clean_objdump(self.pathToFile)
    
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