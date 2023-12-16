from utils.enum.ArgumentsEnum import Arguments
from utils.abstract.Default import DefaultTask

class HelpTask(DefaultTask):

    def defineTask(self) -> None:
        self.__printHelpMessage()
    
    def __printHelpMessage(self) -> None:
        """_summary_
        """
        
        print("Uso: python main.py [opciones]")
        print("Opciones disponibles:")
        for arg in Arguments:
            print("     " + str(arg))