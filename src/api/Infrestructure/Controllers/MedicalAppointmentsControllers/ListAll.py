from src.api.Application.UseCase.MedicalAppointmentsUseCase.ListAll import ListAll as UseCase
from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort as Port


class ListAllController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self,IdBaby):
        print("Listando citas medicas")
        return self.use_case.run(IdBaby)
