from abc import ABC, abstractmethod
from main.log.LogManagerClass import LogManager

from abc import ABC, abstractmethod

class DefaultTask(ABC):
    """Base class for defining default tasks.

    This class provides a template for defining tasks by subclassing it.
    Subclasses must implement the `defineTask` method.

    Args:
        arg_command (str, optional): The command argument for the task. Defaults to "".
    """

    def __init__(self, arg_command: str = ""):
        """Initialize the DefaultTask instance.

        Args:
            arg_command (str, optional): The command argument for the task. Defaults to "".
        """

        super().__init__()
        self.logManager = LogManager()
        self.arg_command = arg_command

    def run(self) -> None:
        """Run the task.

        This method logs the execution of the task and calls the `defineTask` method.
        """

        self.logManager.log("Ejecutando tarea: " + self.__class__.__name__)
        self.defineTask()

    @abstractmethod
    def defineTask(self) -> None:
        """Define the task.

        This method must be implemented by subclasses to define the specific task logic.
        """

        pass
