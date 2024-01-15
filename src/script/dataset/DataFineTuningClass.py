

class DataFineTuning:
    """A class representing data for fine-tuning.

    This class stores information related to fine-tuning data, including an instruction,
    input data, and output data. It provides methods to set and retrieve these values.

    Attributes:
        __instruction (str): The instruction for fine-tuning.
        __input (str): The input data for fine-tuning.
        __output (str): The output data for fine-tuning.
    """
    
    def __init__(self) -> None:
        """Initialize a new instance of the DataFineTuning class."""
        
        self.__instruction = "Generate a C code from this assembler code"
        self.__input = ""
        self.__output = ""
    
    def setInstruction(self, instruction: str) -> None:
        """Set the instruction for fine-tuning.

        Args:
            instruction (str): The instruction to set.
        """
        
        self.__instruction = instruction
    
    def setInput(self, input: str) -> None:
        """Set the input data for fine-tuning.

        Args:
            input (str): The input data to set.
        """
        
        self.__input = input
    
    def setOutput(self, output: str) -> None:
        """Set the output data for fine-tuning.

        Args:
            output (str): The output data to set.
        """
        
        self.__output = output
    
    def getDataFineTuningJSON(self) -> dict[str, str]:
        """Get the data for fine-tuning as a JSON object.

        Returns:
            dict[str, str]: A dictionary representing the data for fine-tuning.
        """
        
        json_data = {
            "instruction": self.__instruction,
            "input": self.__input,
            "output": self.__output
        }

        return json_data