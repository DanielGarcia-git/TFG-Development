from main.command.ConfigurationClass import Configuration
from utils.enum.ArgumentsEnum import Arguments

from main.tasks.Help import HelpTask
from main.tasks.Version import VersionTask
from main.tasks.RepositorySetup import RepositorySetupTask

import sys

class CommandProcessor:
    """_summary_
    """

    __instance = None

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.__instance = super(CommandProcessor, self).__new__(self)
        return self.__instance

    def processArgumentList(self, argumentList: list[str]) -> None:
        """_summary_

        Args:
            argumentList (list[str]): _description_
        """
        
        config = Configuration()

        for argument in argumentList:
            arg = config.isArgAvailable(argument)
            if arg is not None:
                config.enableArg(arg)
            else:
                print(f"El argumento {argument} no se reconoce. Prueba con -h o --help para más información.")
                sys.exit(1)    
    
    def executeTasksReletedWithArgs(self) -> None:
        """_summary_
        """

        config = Configuration()

        if config.getArg(Arguments.HELP):
            helpTask = HelpTask()
            helpTask.run()
            return
        if config.getArg(Arguments.VERSION):
            verionTask = VersionTask()
            verionTask.run()
            return
        if config.getArg(Arguments.REPOSITORY_SETUP):
            repositorySetupTask = RepositorySetupTask()
            repositorySetupTask.run()

        
        