from src.api.Application.UseCase.MedicalAppointmentsUseCase.Delete import Delete as UseCase
from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort as Port


class DeleteController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self,IdMedicalAppointment):
        return self.use_case.run(IdMedicalAppointment)
