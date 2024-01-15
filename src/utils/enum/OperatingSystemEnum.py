from enum import Enum, auto

class OperatingSystem(Enum):
    """Represents the operating system types."""

    WINDOWS = auto()
    LINUX = auto()
    NONE = auto()