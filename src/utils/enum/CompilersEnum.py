from enum import Enum

from enum import Enum

class Compilers(Enum):
    """An enumeration of different compilers.
    
    This enumeration represents different compilers that can be used in a software development project.
    Each compiler is associated with a specific command or executable name.
    """

    VISUAL_STUDIO = "cl"
    GCC = "gcc"
    NONE = ""