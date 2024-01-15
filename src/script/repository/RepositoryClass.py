import shutil
import os

from git import Repo
from utils.enum.PathsEnum import Paths
from utils.enum.RepositoryTypeEnum import RepositoryType
from main.log.LogManagerClass import LogManager

class Repository:
    """A class representing a repository.

    Attributes:
        __nameRepo (str): The name of the repository.
        __urlRepo (str): The URL of the repository.
        __pathToLocalRepository (str): The local path to the repository.
        __repo (Repo): The Git repository object.
    """

    def __init__(self, name: str, url: str, type: str) -> None:
        """Initialize a Repository object.

        Args:
            name (str): The name of the repository.
            url (str): The URL of the repository.
            type (str): The type of the repository.
        """

        self.__logManager = LogManager()
        self.__nameRepo = name
        self.__urlRepo = url
        if type == str(RepositoryType.REPOSITORY_CODE_C.value):
            self.__pathToLocalRepository = str(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value) + os.sep + self.__nameRepo
        
        if not shutil.os.path.exists(self.__pathToLocalRepository):
            self.__logManager.log("Clonando repositorio " + self.__nameRepo + " en " + self.__pathToLocalRepository)
            self.__repo = Repo.clone_from(self.__urlRepo, self.__pathToLocalRepository)
        else:
            self.__logManager.log("Repositorio " + self.__nameRepo + " ya existe en " + self.__pathToLocalRepository)
            self.__repo = Repo(self.__pathToLocalRepository)
    
    def __str__(self) -> str:
        """Return the name of the repository.

        Returns:
            str: The name of the repository.
        """

        return self.__nameRepo