from io import TextIOWrapper

class CodeFile:
    '''
    '''
    
    def __init__(self) -> None:
        self.__codeFile = TextIOWrapper
        self.__pathToFile = ""

    def setPathToFile(self, newPath: str) -> None:
        self.__pathToFile = newPath
        self.__codeFile = open(self.__pathToFile, 'r')

    def getData(self) -> list[str]:
        return self.__codeFile.readlines()