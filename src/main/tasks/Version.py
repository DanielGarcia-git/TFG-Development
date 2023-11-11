from main.tasks.Default import DefaultTask
from main.command.ConfigurationClass import Configuration

class VersionTask(DefaultTask):

    def defineTask(self) -> None:
        self.__printVersionMessage()
    
    def __printVersionMessage(self) -> None:
        """_summary_
        """
        
        config = Configuration()
        print("Version " + config.getVersion())