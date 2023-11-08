from main.command.CommandProcessorClass import CommandProcessor
from main.log.LogManagerClass import LogManager

import sys


def main():
    """_summary_
    """
    logManager = LogManager()
    logManager.log("Starting program...")
    cmdProcesor = CommandProcessor()
    logManager.log("Processing arguments...")
    cmdProcesor.processArgumentList(sys.argv[1:])
    logManager.log("Executing tasks..." + str(cmdProcesor.getListOfTasks()))
    cmdProcesor.executeTasks()

if __name__ == '__main__':
    sys.path.append("C:/Users/dani_/Documents/MEGAsync/UPC/Q9/TFG/Development/TFG-Development/src")
    sys.exit(main())