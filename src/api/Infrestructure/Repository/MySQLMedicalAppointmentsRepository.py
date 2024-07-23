from src.api.Domain.Entity.MedicalAppointments import MedicalAppointments
from src.api.Domain.Ports.MedicalAppointmentsPort import MedicalAppointmentsPort
from src.Database.MySQL import Base, engine, session_local
from sqlalchemy.orm import joinedload
from src.api.Infrestructure.Models.MySQLMedicalAppointmentsModel import MySQLMedicalAppointmentsModel as Model
import json

import datetime

# Crear una instancia de datetime.date

class MySQLMedicalAppointmentsRepository(MedicalAppointmentsPort):
    
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_all_medical_appointments(self,IdBaby):
        try:            
            citas = self.db.query(Model).filter(Model.IdBaby == IdBaby).all()
            value = []            
            for item in citas:
                value.append({
                    "IdMedicalAppointment":item.IdMedicalAppointment,
                    "IdBaby":item.IdBaby,
                    "title":item.title,
                    "date":str(item.date),
                    "description":item.description,
                    "hour" : str(item.hour),
                    "active":item.active
                })
            if citas:
                return {
                    "error":False,
                    "status": 200,
                    "message": f"Se encontraron {len(value)} citas medicas",                                        
                    "value": value,
                },
            else:
                return {
                    "error":False,
                    "status": 404,
                    "message": "No se encontraron citas medicas",                     
                    "value":[]
                    },
        except Exception as e:
            return {"message": str(e), "status": "error"},

    def create_cita(self, cita: MedicalAppointments):
        try:
            if(cita['IdMedicalAppointment'] == 0):
                print("Crear")
                new = Model(
                    IdMedicalAppointment=cita['IdMedicalAppointment'],
                    IdBaby=cita['IdBaby'],
                    title=cita['title'],
                    date=cita['date'],
                    description=cita['description'],
                    hour=cita['hour'],
                    active=1
                )
                self.db.add(new)
                self.db.commit()            
                return {
                        "error":False,
                        "status": 200,
                        "message": "Cita guardada", 
                    },
            else:
                print("actualizar")
                existing_cita = self.db.query(Model).filter_by(IdMedicalAppointment=cita['IdMedicalAppointment']).first()
                existing_cita.active = 0
                self.db.commit()

                print(existing_cita)           
                return {
                        "error":False,
                        "status": 200,
                        "message": "Cita guardada", 
                    },
                
        except Exception as e:
            return {"error":True, "status": 500,"message": str(e)}, 
        
    def delete(self,IdMedicalAppointment):
        
        try:
            print(IdMedicalAppointment)
            appointment = self.db.query(Model).filter(Model.IdMedicalAppointment == IdMedicalAppointment).first()
            if appointment:
                self.db.delete(appointment)
                self.db.commit()
                return {
                    "error": False,
                    "status": 200,
                    "message": "Dato eliminado",
                }
            
            return {
                    "error":False,
                    "status": 200,
                    "message": "Dato eliminado", 
                },
        except Exception as e:
            return {
                    "error":True,
                    "status": 500,
                    "message": e, 
                },

