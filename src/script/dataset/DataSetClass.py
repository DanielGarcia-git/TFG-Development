import json
import os

from script.dataset.DataFineTuningClass import DataFineTuning
from utils.enum.PathsEnum import Paths
from main.log.LogManagerClass import LogManager

class DataSet:
    """A class representing a dataset.

    This class provides methods to add data to the dataset, retrieve the dataset, and export the dataset to a JSON file.

    Attributes:
        __instance (DataSet): The singleton instance of the DataSet class.
        __dataSet (list): The list of data in the dataset.
    """

    __instance = None
    __dataSet = []

    def __new__(self):
        """Creates a new instance of the DataSet class.

        Returns:
            DataSet: The DataSet instance.
        """

        if not self.__instance:
            self.__instance = super(DataSet, self).__new__(self)
            self.__logManager = LogManager()
        return self.__instance
    
    def __str__(self) -> str:
        """Returns a string representation of the dataset.

        Returns:
            str: The string representation of the dataset.
        """
        
        return str(self.__dataSet)

    def addData(self, data: DataFineTuning) -> None:
        """Adds data to the dataset.

        Args:
            data (DataFineTuning): The data to be added to the dataset.
        """
        
        self.__dataSet.append(data)
    
    def getDataSet(self) -> list:
        """Returns the dataset.

        Returns:
            list: The dataset.
        """
        
        return self.__dataSet
    
    def exportDataSet(self) -> None:
        """Exports the dataset to a JSON file.

        Args:
            path (str): The path to export the dataset.
        """
        
        self.__logManager.log(f"Exporting dataset to {str(Paths.PATH_TO_DATASET.value)}")
        if not os.path.exists(str(Paths.PATH_TO_DATASET.value)):
            os.makedirs(str(Paths.PATH_TO_DATASET.value))
        
        with open(str(Paths.PATH_TO_DATASET.value) + os.sep + "dataSet.json", 'w') as outfile:
            outfile.write("[")
            for i, data in enumerate(self.__dataSet):
                outfile.write(json.dumps(data.getDataFineTuningJSON()))
                if i != len(self.__dataSet) - 1:
                    outfile.write(",")
            outfile.write("]")
