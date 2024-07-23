from src.api.Application.UseCase.ChatUseCase.ListAll import ListAll as UseCase
from src.api.Domain.Ports.ChatPort import ChatPort as Port


class ListAllController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
