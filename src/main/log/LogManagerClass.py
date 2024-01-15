import datetime
import logging
import os
import shutil
import colorlog
from utils.enum.PathsEnum import Paths
from main.command.ConfigurationClass import Configuration
from utils.enum.ArgumentsEnum import Arguments

class LogManager:
    """
    The LogManager class provides a centralized logging functionality for the application.

    Attributes:
        __instance (LogManager): The singleton instance of the LogManager class.

    Methods:
        __new__(self): Creates a new instance of the LogManager class.
        __createLogDir(self) -> None: Creates the log directory if it doesn't exist.
        log(self, message: str) -> None: Logs an informational message.
        logError(self, message: str) -> None: Logs an error message.
        logWarning(self, message: str) -> None: Logs a warning message.
        logDebug(self, message: str) -> None: Logs a debug message.
    """

    __instance = None

    def __new__(self):
        """
        Creates a new instance of the LogManager class.

        Returns:
            LogManager: The LogManager instance.
        """

        if not self.__instance:
            self.__instance = super(LogManager, self).__new__(self)
            self.__config = Configuration()
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            formatter = colorlog.ColoredFormatter(
                '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
                log_colors={
                    'DEBUG': 'reset',
                    'INFO': 'reset',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'red,bg_white',
                },
                secondary_log_colors={},
                style='%'
            )
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
            self.__createLogDir(self)
            now = datetime.datetime.now()
            log_file_name = now.strftime("%Y-%m-%d_%H-%M-%S_log.txt")
            print(Paths.PATH_TO_LOG_DIR.value)
            fh = logging.FileHandler(os.path.join(Paths.PATH_TO_LOG_DIR.value, log_file_name))
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        return self.__instance
    
    def __createLogDir(self) -> None:
        """
        Creates the log directory if it doesn't exist.
        """

        if not shutil.os.path.exists(str(Paths.PATH_TO_LOG_DIR.value)):
            os.makedirs(str(Paths.PATH_TO_LOG_DIR.value))

    def log(self, message: str) -> None:
        """
        Logs an informational message.

        Args:
            message (str): The message to be logged.
        """

        self.logger.info(message)
    
    def logError(self, message: str) -> None:
        """
        Logs an error message.

        Args:
            message (str): The error message to be logged.
        """

        self.logger.error(message)
    
    def logWarning(self, message: str) -> None:
        """
        Logs a warning message.

        Args:
            message (str): The warning message to be logged.
        """

        self.logger.warning(message)

    def logDebug(self, message: str) -> None:
        """
        Logs a debug message.

        Args:
            message (str): The debug message to be logged.
        """

        if self.__config.getArg(Arguments.DEBUG):
            self.logger.debug(message)
