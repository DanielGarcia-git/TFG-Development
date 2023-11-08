from main.command.ConfigurationClass import Configuration
from utils.enum.ArgumentsEnum import Arguments

from main.tasks.Help import HelpTask
from main.tasks.Version import VersionTask
from main.tasks.RepositorySetup import RepositorySetupTask
from main.tasks.Compiler import CompilerTask

import sys

class CommandProcessor:
    """_summary_
    """

    __instance = None
    __tasksArray = []

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
                self.__addTask(arg)
            else:
                print(f"El argumento {argument} no se reconoce. Prueba con -h o --help para más información.")
                sys.exit(1)    
    
    def __addTask(self, arg: Arguments) -> None:
        """_summary_
        """

        if arg == Arguments.HELP:
            self.__tasksArray.append(HelpTask())
        elif arg == Arguments.VERSION:
            self.__tasksArray.append(VersionTask())
        elif arg == Arguments.REPOSITORY_SETUP:
            self.__tasksArray.append(RepositorySetupTask())
        elif arg == Arguments.COMPILER_SETUP:
            self.__tasksArray.append(CompilerTask())
        
    def getListOfTasks(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        
        return self.__tasksArray
    
    def executeTasks(self) -> None:
        """_summary_
        """
        
        for task in self.__tasksArray:
            task.run()

        
        