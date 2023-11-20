from main.tasks.Default import DefaultTask
from utils.enum.PathsEnum import Paths
from script.ia.lit_gpt.LitGPTUtilsClass import LitGPTUtils

class ListAvailableModelsTask(DefaultTask):

    def defineTask(self) -> None:

        models = LitGPTUtils.getLitGPTAvailableModels()

        if len(models) > 0:
            print("Listado de modelos disponibles:")
            for model in models:
                print(f"\t- {model}")
        else:
            self.logManager.logError("No se han encontrado modelos disponibles o ha ocurrido un error al obtenerlos")