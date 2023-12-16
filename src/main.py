from main.command.CommandProcessorClass import CommandProcessor
from main.log.LogManagerClass import LogManager

import sys


def main():
    """_summary_
    """
    logManager = LogManager()
    logManager.log("Empezando el programa...")
    cmdProcesor = CommandProcessor()
    logManager.logDebug("Procesando los argumentos: " + str(sys.argv[1:]))
    cmdProcesor.processArgumentList(sys.argv[1:])
    logManager.logDebug("Tareas definidas: " + str(cmdProcesor.getListOfTasks()))
    cmdProcesor.executeTasks()

if __name__ == '__main__':
    sys.path.append("C:/Users/dani_/Documents/MEGAsync/UPC/Q9/TFG/Development/TFG-Development/src")
    sys.exit(main())