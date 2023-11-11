from script.repository.RepositoryClass import Repository

class RepositoryList:
    """_summary_
    """

    __instance = None
    __pathToRepositoryFile = ""
    __repositorySet = set()

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.__instance = super(RepositoryList, self).__new__(self)
        return self.__instance

    def setRepositoryListByFile(self, pathToFile: str) -> None:
        """_summary_

        Args:
            pathToFile (str): _description_
        """

        self.__pathToRepositoryFile = pathToFile
        self.__repositorySet.clear()

        with open(self.__pathToRepositoryFile, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    self.__repositorySet.add(Repository(line))

        
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
