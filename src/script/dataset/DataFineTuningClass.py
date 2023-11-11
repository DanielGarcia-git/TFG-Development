
import json


class DataFineTuning:
    
    def __init__(self) -> None:
        """_summary_
        """
        
        self.__instruction = "Generate a C code from this assembler code"
        self.__input = ""
        self.__output = ""
    
    def setInstruction(self, instruction: str) -> None:
        """_summary_

        Args:
            instruction (str): _description_
        """
        
        self.__instruction = instruction
    
    def setInput(self, input: str) -> None:
        """_summary_

        Args:
            input (str): _description_
        """
        
        self.__input = input
    
    def setOutput(self, output: str) -> None:
        """_summary_

        Args:
            output (str): _description_
        """
        
        self.__output = output
    
    def getDataFineTuningJSON(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        
        return "{\"instruction\": \"" + self.__instruction + "\", \"input\": \"" + self.__input + "\", \"output\": \"" + self.__output + "\"}"