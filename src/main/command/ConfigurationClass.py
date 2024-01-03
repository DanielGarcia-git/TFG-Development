from utils.enum.ArgumentsEnum import Arguments

class Configuration:
    """This class represents the actual configuration of the system. Stores things like
       which arguments are activated.

       This class follows the singleton pattern.
    """

    __instance = None
    __configurationArgs = {args: False for args in Arguments}
    __version = "0.0.1"

    def __new__(self):
        """If the Configuration instance doesn't exist, this function creates a new one,
           otherwise, returns the actual instance

        Returns:
            Configuration: The unique instance of the Configuration class
        """

        if not self.__instance:
            self.__defaultConfiguration(self)
            self.__instance = super(Configuration, self).__new__(self)
        return self.__instance
    
    def __defaultConfiguration(self) -> None:
        """This function sets the default configuration in the system. Usually, this
           function is used to initialize the configuration system.
        """

        self.__configurationArgs[Arguments.HELP] = True
        self.__configurationArgs[Arguments.VERSION] = False
        self.__configurationArgs[Arguments.REPOSITORY_SETUP] = False
        self.__configurationArgs[Arguments.COMPILER_SETUP] = False
        self.__configurationArgs[Arguments.DATASET_SETUP] = False
        self.__configurationArgs[Arguments.DEBUG] = False
        self.__configurationArgs[Arguments.CLEAN_UP] = False

    def isArgAvailable(self, arg: str) -> Arguments:
        """This function returns the state of one specific argument, in other words,
           if this argument is activated  or not.

        Args:
            arg (Arguments): The argument to be check

        Returns:
            bool: Returns True if the argument is activated, otherwise, returns False
        """

        for availableArg in self.__configurationArgs:
            if arg == availableArg.getArgShort() or arg == availableArg.getArgLarge():
                return availableArg
            
        return None


    def enableArg(self, arg: Arguments) -> None:
        """This function activates an argument.

        Args:
            arg (Arguments): The argument to be activated
        """
        
        if arg != Arguments.HELP:
            self.__configurationArgs[Arguments.HELP] = False
        
        self.__configurationArgs[arg] = True

    def disableArg(self, arg: Arguments) -> None:
        """This function deactivates an argument

        Args:
            arg (Arguments): The argument to be deactivated
        """

        self.__configurationArgs[arg] = False
    
    def getArg(self, arg: Arguments) -> bool:
        """This function returns the state of an argument

        Args:
            arg (Arguments): The argument to get the state

        Returns:
            bool: Retunrs the state of the argument
        """

        return self.__configurationArgs[arg]
    
    def getVersion(self) -> str:
        """This function returns the version of the system

        Returns:
            str: A String representing the version of the system
        """

        return self.__version