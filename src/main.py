from main.command.CommandProcessorClass import CommandProcessor

import sys


def main():
    """_summary_
    """

    cmdProcesor = CommandProcessor()
    cmdProcesor.processArgumentList(sys.argv[1:])
    cmdProcesor.executeTasksReletedWithArgs()

if __name__ == '__main__':
    sys.path.append("C:/Users/dani_/Documents/MEGAsync/UPC/Q9/TFG/Development/TFG-Development/src")
    sys.exit(main())