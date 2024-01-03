from utils.abstract.Default import DefaultTask
from script.repository.RepositoryListClass import RepositoryList
from utils.enum.PathsEnum import Paths

class RepositorySetupTask(DefaultTask):
    """This class implements the task that downloads the repositories
    """

    def __init__(self):
        """The default constructor of RepositorySetupTask
        """

        super().__init__()
        self.__repositoryList = RepositoryList()

    def defineTask(self) -> None:
        """This function defines the behaivor of the task, in this case
           downloads all the repositories
        """

        self.logManager.log("Definiendo los repositorios mediante un fichero " + str(Paths.PATH_TO_REPOSITORY_LIST.value))
        self.__repositoryList.setRepositoryListByFile(str(Paths.PATH_TO_REPOSITORY_LIST.value))