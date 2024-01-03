from utils.enum.ArgumentsEnum import Arguments
from utils.abstract.Default import DefaultTask

class HelpTask(DefaultTask):
    """ This class implements the task that print the help message.
    """

    def defineTask(self) -> None:
        """This function defines the behaivor of the task, in this case
           prints the help message.
        """

        self.__printHelpMessage()
    
    def __printHelpMessage(self) -> None:
        """This function prints the help message
        """
        
        print("Uso: python main.py [opciones]")
        print("Opciones disponibles:")
        for arg in Arguments:
            print("     " + str(arg))