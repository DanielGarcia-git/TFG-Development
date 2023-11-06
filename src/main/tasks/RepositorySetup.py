from main.tasks.Default import DefaultTask

class RepositorySetupTask(DefaultTask):

    def run(self) -> None:
        print("RepositorySetupTask")