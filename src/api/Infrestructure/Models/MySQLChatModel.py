from sqlalchemy import Column, String, Integer, Date,Time
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base



class MySQLChatModel(Base):
    
    __tablename__ = 'lkp_chat'
    
    IdChat = Column(Integer, primary_key=True,index=True)
    IdUser = Column(Integer, nullable=True)
    date = Column(Date, nullable=True)
    hour = Column(Time(255), nullable=True)
    text = Column(String(250), nullable=True)
    username = Column(String(250), nullable=True)

    def to_json(self):
        return {
            "IdChat": self.IdChat,
            "IdUser": self.IdUser,
            "date": str(self.date),
            "hour": str(self.hour),
            'text': self.text,    
            'username': self.username,            
        }

