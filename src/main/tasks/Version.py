from utils.abstract.Default import DefaultTask
from main.command.ConfigurationClass import Configuration

class VersionTask(DefaultTask):
    """ This class implements the task that print the version message.
    """

    def defineTask(self) -> None:
        """This function defines the behaivor of the task, in this case
           prints the version message.
        """
        
        self.__printVersionMessage()
    
    def __printVersionMessage(self) -> None:
        """This function prints the version message
        """
        
        config = Configuration()
        print("Version " + config.getVersion())