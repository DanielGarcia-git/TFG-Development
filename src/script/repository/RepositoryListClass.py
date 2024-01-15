from script.repository.RepositoryClass import Repository
import json

class RepositoryList:
    """A class representing a list of repositories.

    This class is implemented as a singleton, meaning that only one instance of it can exist at a time.
    It provides methods to set the repository list from a file and store the repositories in a set.

    Attributes:
        __instance (RepositoryList): The singleton instance of the RepositoryList class.
        __pathToRepositoryFile (str): The path to the repository file.
        __repositorySet (set): The set of repositories.

    """

    __instance = None
    __pathToRepositoryFile = ""
    __repositorySet = set()

    def __new__(self):
        """Creates a new instance of the RepositoryList class.

        Returns:
            RepositoryList: The RepositoryList instance.

        """

        if not self.__instance:
            self.__instance = super(RepositoryList, self).__new__(self)
        return self.__instance

    def setRepositoryListByFile(self, pathToFile: str) -> None:
        """Sets the repository list by reading from a file.

        Args:
            pathToFile (str): The path to the repository file.

        """

        self.__pathToRepositoryFile = pathToFile
        self.__repositorySet.clear()

        jsonFile = open(pathToFile, "r")
        jsonObject = json.load(jsonFile)

        for repository in jsonObject["repositories"]:
            self.__repositorySet.add(Repository(repository["name"], repository["url"], repository["type"]))
