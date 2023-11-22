from utils.enum.ArgumentsEnum import Arguments

class Configuration:
    """_summary_
    """

    __instance = None
    __configurationArgs = {args: False for args in Arguments}
    __version = "0.0.1"

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.__defaultConfiguration(self)
            self.__instance = super(Configuration, self).__new__(self)
        return self.__instance
    
    def __defaultConfiguration(self) -> None:
        """_summary_
        """

        self.__configurationArgs[Arguments.HELP] = True
        self.__configurationArgs[Arguments.VERSION] = False
        self.__configurationArgs[Arguments.REPOSITORY_SETUP] = False
        self.__configurationArgs[Arguments.COMPILER_SETUP] = False
        self.__configurationArgs[Arguments.DATASET_SETUP] = False
        self.__configurationArgs[Arguments.DEBUG] = False
        self.__configurationArgs[Arguments.CLEAN_UP] = False
        self.__configurationArgs[Arguments.FINETUNING] = False
        self.__configurationArgs[Arguments.IA_SETUP] = False
        self.__configurationArgs[Arguments.LIST_AVAILABLE_MODELS] = False
        self.__configurationArgs[Arguments.LIST_AVAILABLE_FINETUNING] = False

    def isArgAvailable(self, arg: str) -> Arguments:
        """_summary_

        Args:
            arg (Arguments): _description_

        Returns:
            bool: _description_
        """

        for availableArg in self.__configurationArgs:
            if arg == availableArg.getArgShort() or arg == availableArg.getArgLarge():
                return availableArg
            
        return None


    def enableArg(self, arg: Arguments) -> None:
        """_summary_

        Args:
            arg (Arguments): _description_
        """
        
        if arg != Arguments.HELP:
            self.__configurationArgs[Arguments.HELP] = False
        
        self.__configurationArgs[arg] = True

    def disableArg(self, arg: Arguments) -> None:
        """_summary_

        Args:
            arg (Arguments): _description_
        """

        self.__configurationArgs[arg] = False
    
    def getArg(self, arg: Arguments) -> bool:
        """_summary_

        Args:
            arg (Arguments): _description_

        Returns:
            bool: _description_
        """

        return self.__configurationArgs[arg]
    
    def getVersion(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self.__version