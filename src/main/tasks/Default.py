from abc import ABC, abstractmethod
from main.log.LogManagerClass import LogManager

class DefaultTask(ABC):
    """_summary_
    """

    def __init__(self, arg_command: str = ""):
        """_summary_

        Args:
            arg_command (str, optional): _description_. Defaults to "".
        """

        super().__init__()
        self.logManager = LogManager()
        self.arg_command = arg_command

    def run(self) -> None:
        """_summary_
        """

        self.logManager.log("Ejecutando tarea: " + self.__class__.__name__)
        self.defineTask()

    @abstractmethod
    def defineTask(self) -> None:
        """_summary_
        """

        pass
