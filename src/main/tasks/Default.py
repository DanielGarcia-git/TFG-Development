from abc import ABC, abstractmethod
from main.log.LogManagerClass import LogManager

class DefaultTask(ABC):
    """_summary_
    """

    def __init__(self):
        """_summary_
        """

        super().__init__()
        self.logManager = LogManager()

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
