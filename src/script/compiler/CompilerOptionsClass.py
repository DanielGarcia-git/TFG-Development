
class CompilerOptions:
    """_summary_
    """

    def __init__(self) -> None:
        """_summary_
        """

        self.__optimisationLevel = 0

    def setOptimisationLevel(self, newLevel: int) -> None:
        """_summary_

        Args:
            newLevel (int): _description_
        """

        self.__optimisationLevel = newLevel
    
    def getOptimisationLevel(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """

        return self.__optimisationLevel