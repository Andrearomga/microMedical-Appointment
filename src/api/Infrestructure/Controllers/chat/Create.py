from src.api.Application.UseCase.ChatUseCase.Create import Create as UseCase
from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort as Port


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, data):                
        return self.use_case.run(data.get_json()["chat"])
