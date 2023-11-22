import datetime
import os
import shutil
import subprocess

from main.tasks.Default import DefaultTask
from utils.enum.PathsEnum import Paths
from script.ia.lit_gpt.LitGPTUtilsClass import LitGPTUtils

class IASetupTask(DefaultTask):

    def __checkComandExecution(self, result: subprocess.CompletedProcess[str]) -> bool:
        """_summary_

        Args:
            result (subprocess.CompletedProcess[str]): _description_

        Returns:
            bool: _description_
        """

        if result.returncode == 0:
            self.logManager.log("Comando ejecutado correctamente")
            return True
        else:
            self.logManager.logError("Error al ejecutar el comando")
            return False
    
    def __checkCorrectModelDownload(self, model: str) -> bool:
        """_summary_

        Args:
            model (str): _description_

        Returns:
            bool: _description_
        """

        models = LitGPTUtils.getLitGPTAvailableModels()
        if model not in models:
            self.logManager.logError("El modelo seleccionado no existe")
            return False
        else:
            self.logManager.logDebug(f"El modelo ({model}) seleccionado existe")
            return True

    def setupLitGptRepo(self) -> None:
        """_summary_
        """

        self.logManager.log("Instalando dependencias necesarias para el proyecto lit-gpt")
        res = LitGPTUtils.installDependencies()

        if res:
            self.logManager.log("Dependencias instaladas correctamente")
        else:
            self.logManager.logError("Error al instalar las dependencias")
            exit(1)

        self.logManager.log(f"Descargando el modelo {self.arg_command}")
        self.__checkCorrectModelDownload(self.arg_command)
        res = LitGPTUtils.downloadModel(self.arg_command)

        if res:
            self.logManager.log("Modelo descargado correctamente")
        else:
            self.logManager.logError("Error al descargar el modelo")
            exit(1)

        self.logManager.log("Creando directorio checkpoint para el modelo instalado")
        res = LitGPTUtils.setCheckpointDir(self.arg_command)

        if res:
            self.logManager.log("Directorio checkpoint creado correctamente")
        else:
            self.logManager.logError("Error al crear el directorio checkpoint")
            exit(1)

    def defineTask(self) -> None:
        
        self.setupLitGptRepo()