from abc import ABC, abstractmethod
from typing import List
from src.api.Domain.Entity.MedicalAppointments import MedicalAppointments

class MedicalAppointmentsPort(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_medical_appointments(self):
        pass

    @abstractmethod
    def create_cita(self, camas: List[MedicalAppointments]):
        pass
        
    @abstractmethod
    def delete(self, IdMedicalAppointment):
        pass
