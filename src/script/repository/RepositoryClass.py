from git import Repo
from utils.enum.PathsEnum import Paths
from main.log.LogManagerClass import LogManager
import shutil
from shutil import rmtree

class Repository:
    """_summary_
    """

    def __init__(self, url: str) -> None:
        """_summary_

        Args:
            url (str): _description_
        """

        self.__logManager = LogManager()
        self.__nameRepo = url.split("/")[-1].replace(".git", "")
        self.__pathToLocalRepository = str(Paths.ROOT_PATH_LOCAL_REPOSITORIES.value) + self.__nameRepo
        if not shutil.os.path.exists(self.__pathToLocalRepository):
            self.__logManager.log("Clonando repositorio " + self.__nameRepo + " en " + self.__pathToLocalRepository)
            self.__repo = Repo.clone_from(url, self.__pathToLocalRepository)
        else:
            self.__logManager.log("Repositorio " + self.__nameRepo + " ya existe en " + self.__pathToLocalRepository)
            self.__repo = Repo(self.__pathToLocalRepository)
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self.__nameRepo