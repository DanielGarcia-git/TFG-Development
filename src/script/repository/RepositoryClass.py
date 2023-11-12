from git import Repo
from utils.enum.PathsEnum import Paths
from utils.enum.RepositoryTypeEnum import RepositoryType
from main.log.LogManagerClass import LogManager
import shutil
from shutil import rmtree

class Repository:
    """_summary_
    """

    def __init__(self, name: str, url: str, type: str) -> None:
        """_summary_

        Args:
            name (str): _description_
            url (str): _description_
            type (str): _description_
        """

        self.__logManager = LogManager()
        self.__nameRepo = name
        self.__urlRepo = url
        if type == str(RepositoryType.REPOSITORY_CODE_C.value):
            self.__pathToLocalRepository = str(Paths.ROOT_PATH_LOCAL_CODE_REPOSITORIES.value) + self.__nameRepo
        elif type == str(RepositoryType.REPOSITORY_IA.value):
            self.__pathToLocalRepository = str(Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES.value) + self.__nameRepo
        
        if not shutil.os.path.exists(self.__pathToLocalRepository):
            self.__logManager.log("Clonando repositorio " + self.__nameRepo + " en " + self.__pathToLocalRepository)
            self.__repo = Repo.clone_from(self.__urlRepo, self.__pathToLocalRepository)
        else:
            self.__logManager.log("Repositorio " + self.__nameRepo + " ya existe en " + self.__pathToLocalRepository)
            self.__repo = Repo(self.__pathToLocalRepository)
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self.__nameRepo