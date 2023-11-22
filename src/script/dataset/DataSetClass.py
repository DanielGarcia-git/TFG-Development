import os
from script.dataset.DataFineTuningClass import DataFineTuning
from utils.enum.PathsEnum import Paths
from main.log.LogManagerClass import LogManager
import json

class DataSet:
    """_summary_
    """

    __instance = None
    __dataSet = []

    def __new__(self):
        """_summary_

        Returns:
            CommandProcessor: _description_
        """

        if not self.__instance:
            self.__instance = super(DataSet, self).__new__(self)
            self.__logManager = LogManager()
        return self.__instance
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        
        return str(self.__dataSet)

    def addData(self, data: DataFineTuning) -> None:
        """_summary_

        Args:
            data (Data): _description_
        """
        
        self.__dataSet.append(data)
    
    def getDataSet(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        
        return self.__dataSet
    
    def exportDataSet(self) -> None:
        """_summary_

        Args:
            path (str): _description_
        """
        
        self.__logManager.log(f"Exportando dataset a {str(Paths.PATH_TO_DATASET.value)}")
        if not os.path.exists(str(Paths.PATH_TO_DATASET.value)):
            os.makedirs(str(Paths.PATH_TO_DATASET.value))
        
        with open(str(Paths.PATH_TO_DATASET.value) + "dataSet.json", 'w') as outfile:
            outfile.write("[")
            for i, data in enumerate(self.__dataSet):
                outfile.write(json.dumps(data.getDataFineTuningJSON()))
                if i != len(self.__dataSet) - 1:
                    outfile.write(",")
            outfile.write("]")
