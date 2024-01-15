import os

from enum import Enum

class Paths(Enum):
    """Enum class that represents various paths used in the application.

    Attributes:
        ROOT_PATH (str): The root path of the application.
        PATH_TO_REPOSITORY_LIST (str): The path to the repository list JSON file.
        PATH_TO_COMPILER_OPTIONS (str): The path to the compiler options JSON file.
        PATH_TO_LOG_DIR (str): The path to the log directory.
        PATH_TO_OUTPUT (str): The path to the output directory.
        ROOT_PATH_LOCAL_CODE_REPOSITORIES (str): The root path of the local code repositories.
        PATH_TO_COMPILER_EXE_OUTPUT (str): The path to the compiler executable output directory.
        PATH_TO_COMPILER_OBJ_OUTPUT (str): The path to the compiler object output directory.
        PATH_TO_COMPILER_ASM_OUTPUT (str): The path to the compiler assembly output directory.
        PATH_TO_COMPILER_OBJDUMP_OUTPUT (str): The path to the compiler objdump output directory.
        PATH_TO_DATASET (str): The path to the dataset directory.
    """
    
    ROOT_PATH = os.getcwd()
    # Data directories
    PATH_TO_REPOSITORY_LIST = os.path.join(ROOT_PATH, "data", "repositories", "repositoryList.json")
    PATH_TO_COMPILER_OPTIONS = os.path.join(ROOT_PATH, "data", "compiler", "compilerOptions.json")
    # Log directories
    PATH_TO_LOG_DIR = os.path.join(ROOT_PATH, "log")
    # Output directories
    PATH_TO_OUTPUT = os.path.join(ROOT_PATH, "output")
    ROOT_PATH_LOCAL_CODE_REPOSITORIES = os.path.join(PATH_TO_OUTPUT, "localRepositories")
    PATH_TO_COMPILER_EXE_OUTPUT = os.path.join(PATH_TO_OUTPUT, "compiler", "exe")
    PATH_TO_COMPILER_OBJ_OUTPUT = os.path.join(PATH_TO_OUTPUT, "compiler", "obj")
    PATH_TO_COMPILER_ASM_OUTPUT = os.path.join(PATH_TO_OUTPUT, "compiler", "asm")
    PATH_TO_COMPILER_OBJDUMP_OUTPUT = os.path.join(PATH_TO_OUTPUT, "compiler", "objdump")
    PATH_TO_DATASET = os.path.join(PATH_TO_OUTPUT, "dataset")
