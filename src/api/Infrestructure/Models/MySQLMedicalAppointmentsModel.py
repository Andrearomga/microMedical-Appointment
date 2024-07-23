from sqlalchemy import Column, String, Integer, Date,Time
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base



class MySQLMedicalAppointmentsModel(Base):
    
    __tablename__ = 'lkp_medical-appointment'
    
    IdMedicalAppointment = Column(Integer, primary_key=True,index=True)
    IdBaby = Column(Integer, nullable=True)
    title = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)
    date = Column(Date, nullable=True)
    hour = Column(Time, nullable=True)
    active = Column(Integer, nullable=True)

    def to_json(self):
        return {
            "IdMedicalAppointment": self.IdMedicalAppointment,
            "IdBaby": self.IdBaby,
            "title": self.title,
            "description": self.description,
            'date': self.date,
            'hour': str(self.hour),
            "active": self.active,
        }

