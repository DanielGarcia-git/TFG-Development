from enum import Enum
import os

class Paths(Enum):
    """_summary_
    """

    ROOT_PATH = os.getcwd()
    ROOT_PATH_LOCAL_REPOSITORIES = ROOT_PATH + "\\output\\localRepositories\\"
    PATH_TO_REPOSITORY_LIST = ROOT_PATH + "\\data\\repositoryList.txt"
    PATH_TO_LOG_DIR = ROOT_PATH + "\\output\\log\\"
    PATH_TO_COMPILER_EXE_OUTPUT = ROOT_PATH + "\\output\\compiler\\exe\\"
    PATH_TO_COMPILER_OBJ_OUTPUT = ROOT_PATH + "\\output\\compiler\\obj\\"
    PATH_TO_COMPILER_ASM_OUTPUT = ROOT_PATH + "\\output\\compiler\\asm\\"