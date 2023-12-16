import sys

from main.command.ConfigurationClass import Configuration
from main.log.LogManagerClass import LogManager
from main.tasks.CleanUp import CleanUpTask
from main.tasks.Compiler import CompilerTask
from main.tasks.DataSet import DataSetTask
from main.tasks.Help import HelpTask
from main.tasks.RepositorySetup import RepositorySetupTask
from main.tasks.Version import VersionTask
from utils.enum.ArgumentsEnum import Arguments

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
            self.__logManager = LogManager()
        return self.__instance

    def processArgumentList(self, argumentList: list[str]) -> None:
        """_summary_

        Args:
            argumentList (list[str]): _description_
        """
        
        config = Configuration()
        processingCommandArg = False
        arg = None

        self.__logManager.logDebug(f"Argumentos recibidos: {argumentList}")

        for argument in argumentList:
            
            if processingCommandArg:
                self.__logManager.logDebug(f"Procesando argumento de comando: {argument}")
                processingCommandArg = False
                self.__addTask(arg, argument)
            else:
                self.__logManager.logDebug(f"Procesando argumento: {argument}")
                arg = config.isArgAvailable(argument)

                processingCommandArg = arg.getHasArg()

                if arg is not None:
                    config.enableArg(arg)
                else:
                    print(f"El argumento {argument} no se reconoce. Prueba con -h o --help para más información.")
                    sys.exit(1)
                
                if not processingCommandArg:
                    self.__addTask(arg, "")
        
        # Si esta variable es cierta significa que no hemos recibido el argumento de comando que es necesario
        if processingCommandArg:
            self.__addTask(arg, "")
    
    def __addTask(self, arg: Arguments, arg_command: str) -> None:
        """_summary_

        Args:
            arg (Arguments): _description_
            arg_command (str): _description_
        """

        if arg == Arguments.HELP:
            self.__tasksArray.append(HelpTask())
        elif arg == Arguments.VERSION:
            self.__tasksArray.append(VersionTask())
        elif arg == Arguments.REPOSITORY_SETUP:
            self.__tasksArray.append(RepositorySetupTask())
        elif arg == Arguments.COMPILER_SETUP:
            if arg_command == "":
                self.__logManager.logError("El argumento -c/--compiler-setup requiere un argumento, el path al archivo de configuración")
                sys.exit(1)
            else:
                self.__tasksArray.append(CompilerTask(arg_command))
        elif arg == Arguments.DATASET_SETUP:
            self.__tasksArray.append(DataSetTask())
        elif arg == Arguments.CLEAN_UP:
            self.__tasksArray.append(CleanUpTask())
        
    def getListOfTasks(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """

        listOfTasks = []

        for task in self.__tasksArray:
            listOfTasks.append(task.__class__.__name__)
        
        return listOfTasks
    
    def executeTasks(self) -> None:
        """_summary_
        """
        
        for task in self.__tasksArray:
            task.run()

        
        