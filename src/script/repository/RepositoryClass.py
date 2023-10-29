from git import Repo

class Repository:
    """_summary_
    """

    def __init__(self, url: str) -> None:
        """_summary_

        Args:
            url (str): _description_
        """

        self.__url = url
        self.__repo = Repo()
        self.__nameRepo = ""
        self.__pathToLocalRepository = ""
    
    def __initialiceRepository(self) -> None:
        """_summary_
        """

        self.__repo = Repo.clone_from(self.__url, self.__pathToLocalRepository)

    def __setRepoName(self) -> None:
        """_summary_
        """
        
        self.__nameRepo = self.__repo.remotes.origin.url.split('.git')[0].split('/')[-1]