
import datetime
import os
import shutil
import subprocess

from main.command.ConfigurationClass import Configuration
from main.log.LogManagerClass import LogManager
from utils.enum.PathsEnum import Paths
from utils.enum.ArgumentsEnum import Arguments

class LitGPTUtils:
    """_summary_
    """
    
    __logManager = LogManager()
    __configuration = Configuration()

    def __printLog(self, outputFile: str, rootPath: str, result: subprocess.CompletedProcess) -> bool:
        """_summary_

        Args:
            outputFile (str): _description_
            rootPath (str): _description_
            result (subprocess.CompletedProcess): _description_

        Returns:
            bool: _description_
        """

        if not shutil.os.path.exists(rootPath):
            os.makedirs(rootPath)

        self.__logManager.logDebug(f"Imprimiendo el resultado del comando en el archivo {outputFile}")
        res = result.returncode == 0
        with open(f"{rootPath}\\{outputFile}", "w") as file:
            if res:
                file.write(result.stdout)
            else:
                file.write(result.stderr)
        
        return res

    @classmethod
    def getLitGPTAvailableModels(self) -> list[str]:
        """_summary_

        Returns:
            list[str]: _description_
        """

        command = f"python {str(Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES.value)}\\lit-gpt\\scripts\\download.py"
        self.__logManager.logDebug(f"Comando a ejecutar: {command}")
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            output_lines = result.stdout.split('\n')
            return output_lines[1:-1]
        else:
            return []
    
    @classmethod
    def installDependencies(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        
        command_install_dependencies = f"pip install -r {str(Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES.value)}\\lit-gpt\\requirements-all.txt"
        output_file = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")

        self.__logManager.logDebug(f"Comando a ejecutar: {command_install_dependencies}")
        result = subprocess.run(command_install_dependencies, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

        return self.__printLog(self, output_file, str(Paths.PATH_TO_PIP_LOG_DIR.value), result)
    
    @classmethod
    def downloadModel(self, model: str) -> bool:
        """_summary_

        Args:
            model (str): _description_

        Returns:
            bool: _description_
        """

        command = f"python {str(Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES.value)}\\lit-gpt\\scripts\\download.py --repo_id {model}"
        output_file = "download_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")

        self.__logManager.logDebug(f"Comando a ejecutar: {command}")

        result = None
        if self.__configuration.getArg(Arguments.DEBUG):
            result = subprocess.run(command)
            return result.returncode == 0
        else:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return self.__printLog(self, output_file, str(Paths.PATH_TO_LIT_GPT_LOG_DIR.value), result)
        
    @classmethod
    def setCheckpointDir(self, model: str) -> bool:
        """_summary_

        Args:
            model (str): _description_

        Returns:
            bool: _description_
        """

        command = f"python {str(Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES.value)}\\lit-gpt\\scripts\\download.py --checkpoint_dir {str(Paths.ROOT_PATH_LOCAL_IA_REPOSITORIES.value)}\\lit-gpt\\checkpoints\\{model}"
        output_file = "checkpoint_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")

        self.__logManager.logDebug(f"Comando a ejecutar: {command}")

        result = None
        if self.__configuration.getArg(Arguments.DEBUG):
            result = subprocess.run(command)
            return result.returncode == 0
        else:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return self.__printLog(self, output_file, str(Paths.PATH_TO_LIT_GPT_LOG_DIR.value), result)
