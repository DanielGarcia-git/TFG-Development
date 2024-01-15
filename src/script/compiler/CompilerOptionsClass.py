
class CompilerOptions:
    """Class representing compiler options.

    Attributes:
        __id (str): The ID of the compiler options.
        __options (list): The list of options for the compiler.
    """

    def __init__(self, id: str = "", options: list = []) -> None:
        """Initialize the CompilerOptions object.

        Args:
            id (str, optional): The ID of the compiler options. Defaults to "".
            options (list, optional): The list of options for the compiler. Defaults to [].
        """

        self.__id = id
        self.__options = options
    
    def getId(self) -> str:
        """Get the ID of the compiler options.

        Returns:
            str: The ID of the compiler options.
        """

        return self.__id

    def getOptions(self) -> list[str]:
        """Get the list of options for the compiler.

        Returns:
            list[str]: The list of options for the compiler.
        """

        return self.__options
    
    def setOptions(self, options: list[str]) -> None:
        """Set the list of options for the compiler.

        Args:
            options (list[str]): The list of options for the compiler.
        """

        self.__options = options