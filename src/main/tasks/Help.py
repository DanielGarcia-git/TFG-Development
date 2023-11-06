from utils.enum.ArgumentsEnum import Arguments
from main.tasks.Default import DefaultTask

class HelpTask(DefaultTask):

    def run(self) -> None:
        self.__printHelpMessage()
    
    def __printHelpMessage(self) -> None:
        """_summary_
        """
        print("Uso: python3 main.py [opciones]")
        print("Opciones disponibles:")
        for arg in Arguments:
            print("     " + str(arg))