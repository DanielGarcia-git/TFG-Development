from main.tasks.Default import DefaultTask

class CompilerTask(DefaultTask):

    def run(self) -> None:
        print("Compiling...")