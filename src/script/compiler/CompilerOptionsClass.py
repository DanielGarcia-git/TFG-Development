
class CompilerOptions:
    """_summary_
    """

    def __init__(self, id: str, options: list[str]) -> None:
        """_summary_
        """

        self.__id = id
        self.__options = options
    
    def getId(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self.__id

    def getOptions(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        options = ""

        for option in self.__options:
            options += option + " "

        return options
    
    def setOptions(self, options: list[str]) -> None:
        """_summary_

        Args:
            options (list[str]): _description_
        """

        self.__options = options