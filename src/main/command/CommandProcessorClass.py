
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

        