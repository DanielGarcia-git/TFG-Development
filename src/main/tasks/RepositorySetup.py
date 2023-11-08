from main.tasks.Default import DefaultTask
from script.repository.RepositoryListClass import RepositoryList
from utils.enum.PathsEnum import Paths
from main.log.LogManagerClass import LogManager

class RepositorySetupTask(DefaultTask):

    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.__repositoryList = RepositoryList()
        self.__logManager = LogManager()

    def run(self) -> None:
        self.__logManager.log("Seting up repositories by file set in " + str(Paths.PATH_TO_REPOSITORY_LIST.value))
        self.__repositoryList.setRepositoryListByFile(str(Paths.PATH_TO_REPOSITORY_LIST.value))