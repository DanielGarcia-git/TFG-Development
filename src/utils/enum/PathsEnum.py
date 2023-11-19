from enum import Enum
import os

class Paths(Enum):
    """_summary_
    """

    ROOT_PATH = os.getcwd()
    # Data directories
    PATH_TO_REPOSITORY_LIST = ROOT_PATH + "\\data\\repositories\\repositoryList.json"
    PATH_TO_COMPILER_OPTIONS = ROOT_PATH + "\\data\\compiler\\compilerOptions.json"
    # Output directories
    PATH_TO_OUTPUT = ROOT_PATH + "\\output\\"
    ROOT_PATH_LOCAL_CODE_REPOSITORIES = ROOT_PATH + "\\output\\localRepositories\\code\\"
    ROOT_PATH_LOCAL_IA_REPOSITORIES = ROOT_PATH + "\\output\\localRepositories\\IA\\"
    PATH_TO_LOG_DIR = ROOT_PATH + "\\log\\"
    PATH_TO_COMPILER_EXE_OUTPUT = ROOT_PATH + "\\output\\compiler\\exe\\"
    PATH_TO_COMPILER_OBJ_OUTPUT = ROOT_PATH + "\\output\\compiler\\obj\\"
    PATH_TO_COMPILER_ASM_OUTPUT = ROOT_PATH + "\\output\\compiler\\asm\\"
    PATH_TO_COMPILER_OBJDUMP_OUTPUT = ROOT_PATH + "\\output\\compiler\\objdump\\"
    PATH_TO_COMPILER_PDB_OUTPUT = ROOT_PATH + "\\output\\compiler\\pdb\\"
    PATH_TO_DATASET = ROOT_PATH + "\\output\\dataset\\"