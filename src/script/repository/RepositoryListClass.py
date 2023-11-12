from script.repository.RepositoryClass import Repository
import json

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

        jsonFile = open(pathToFile, "r")
        jsonObject = json.load(jsonFile)

        for repository in jsonObject["repositories"]:
            self.__repositorySet.add(Repository(repository["name"], repository["url"], repository["type"]))

        # Leer un archivo JSON
        # https://www.w3schools.com/python/python_json.asp
        # https://www.geeksforgeeks.org/read-json-file-using-python/
        # https://www.programiz.com/python-programming/json
        # https://www.geeksforgeeks.org/reading-writing-json-python/
        # https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/


        
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
