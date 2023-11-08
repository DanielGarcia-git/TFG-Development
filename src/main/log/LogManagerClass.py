import datetime
import logging
import os
import shutil
from utils.enum.PathsEnum import Paths

class LogManager:
    """_summary_
    """

    __instance = None

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
            self.__createLogDir(self)
            now = datetime.datetime.now()
            log_file_name = now.strftime("%Y-%m-%d_%H-%M-%S_log.txt")
            fh = logging.FileHandler(str(Paths.PATH_TO_LOG_DIR.value) + log_file_name)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.__instance = super(LogManager, self).__new__(self)
        return self.__instance
    
    def __createLogDir(self) -> None:
        """_summary_
        """

        if not shutil.os.path.exists(str(Paths.PATH_TO_LOG_DIR.value)):
            os.makedirs(str(Paths.PATH_TO_LOG_DIR.value))

    def log(self, message: str) -> None:
        """_summary_

        Args:
            message (str): _description_
        """

        self.logger.info(message)
    
    def logError(self, message: str) -> None:
        """_summary_

        Args:
            message (str): _description_
        """

        self.logger.error(message)
    
    def logWarning(self, message: str) -> None:
        """_summary_

        Args:
            message (str): _description_
        """

        self.logger.warning(message)

    def logDebug(self, message: str) -> None:
        """_summary_

        Args:
            message (str): _description_
        """

        self.logger.debug(message)
    

