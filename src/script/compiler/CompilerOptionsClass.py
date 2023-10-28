
class CompilerOptions:
    '''
    '''

    def __init__(self) -> None:
        self.__optimisationLevel = 0

    def setOptimisationLevel(self, newLevel: int) -> None:
        self.__optimisationLevel = newLevel
    
    def getOptimisationLevel(self) -> int:
        return self.__optimisationLevel