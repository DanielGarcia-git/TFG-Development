from enum import Enum
import os

class Paths(Enum):
    """_summary_
    """

    ROOT_PATH = os.getcwd()
    # Data directories
    PATH_TO_REPOSITORY_LIST = os.path.join(os.getcwd(), "data/repositories/repositoryList.json")
    PATH_TO_COMPILER_OPTIONS = os.path.join(os.getcwd(), "data/compiler/compilerOptions.json")
    # Log directories
    PATH_TO_LOG_DIR = os.path.join(os.getcwd(), "log/")
    # Output directories
    PATH_TO_OUTPUT = os.path.join(os.getcwd(), "output/")
    ROOT_PATH_LOCAL_CODE_REPOSITORIES = os.path.join(os.getcwd(), "output/localRepositories/code/")
    PATH_TO_COMPILER_EXE_OUTPUT = os.path.join(os.getcwd(), "output/compiler/exe/")
    PATH_TO_COMPILER_OBJ_OUTPUT = os.path.join(os.getcwd(), "output/compiler/obj/")
    PATH_TO_COMPILER_ASM_OUTPUT = os.path.join(os.getcwd(), "output/compiler/asm/")
    PATH_TO_COMPILER_OBJDUMP_OUTPUT = os.path.join(os.getcwd(), "output/compiler/objdump/")
    PATH_TO_COMPILER_PDB_OUTPUT = os.path.join(os.getcwd(), "output/compiler/pdb/")
    PATH_TO_DATASET = os.path.join(os.getcwd(), "output/dataset/")