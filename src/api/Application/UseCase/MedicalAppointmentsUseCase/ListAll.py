from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort as Port

class ListAll:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self,IdBaby):        
        try:
            return self.repository.get_all_medical_appointments(IdBaby)
        except Exception as e:
            return {"error": str(e), "status": "Unexpected error"}, 500
