from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort as Port
from src.api.Domain.Entity.MedicalAppointments import MedicalAppointments


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):        
        try:
            return self.repository.create_cita(data)
        except Exception as e:
            return {"error": str(e), "status": "Unexpected data"}, 500
