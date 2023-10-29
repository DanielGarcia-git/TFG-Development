
class RepositoryList:
    """_summary_
    """

    def __init__(self) -> None:
        """_summary_
        """
        
        self.__pathToRepositoryFile = ""

    def setRepositoryListByFile(self, pathToFile: str) -> None:
        """_summary_

        Args:
            pathToFile (str): _description_
        """

        self.__pathToRepositoryFile = pathToFile