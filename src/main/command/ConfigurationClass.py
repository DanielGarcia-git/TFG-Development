from utils.enum.ArgumentsEnum import Arguments

class Configuration:
    """_summary_
    """

    __instance = None
    __configurationArgs = {args: False for args in Arguments}

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.__defaultConfiguration()
            self.__instance = super(Configuration, self).__new__(self)
        return self.__instance
    
    def __defaultConfiguration(self) -> None:
        """_summary_
        """

        pass

    def enableArg(self, arg: Arguments) -> None:
        """_summary_

        Args:
            arg (Arguments): _description_
        """

        self.__configurationArgs[arg] = True

    def disableArg(self, arg: Arguments) -> None:
        """_summary_

        Args:
            arg (Arguments): _description_
        """

        self.__configurationArgs[arg] = False