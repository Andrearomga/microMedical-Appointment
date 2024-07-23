from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort as Port

class Delete:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self,IdMedicalAppointment):        
        try:
            return self.repository.delete(IdMedicalAppointment)
        except Exception as e:
            return {"error": str(e), "status": "Unexpected error"}, 500
