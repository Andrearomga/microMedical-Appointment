from src.api.Domain.Entity.Chat import Chat
from src.api.Domain.Ports.ChatPort import ChatPort
from src.Database.MySQL import Base, engine, session_local
from src.api.Infrestructure.Models.MySQLChatModel import MySQLChatModel as Model
import joblib

# Cargar el modelo y el vectorizador desde archivos
try:
    model = joblib.load('./src/api/Infrestructure/Repository/modelo_entrenado.pkl')
    vectorizer = joblib.load('./src/api/Infrestructure/Repository/vectorizer.pkl')
except FileNotFoundError as e:
    print(f"Error al cargar el modelo o el vectorizador: {e}")
    exit()

class MySQLChatRepository(ChatPort):
    
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()
        
    def detectar_groseria(self, texto):
        texto_vectorizado = vectorizer.transform([texto])
        prediccion = model.predict(texto_vectorizado)
        return prediccion[0] == 1  # 1 indica grosería, 0 indica texto limpio

    def save(self, chat: Chat):  
        print(chat)
        text = chat["text"]
        tiene_groseria = self.detectar_groseria(text)
        print(tiene_groseria)
        
        if tiene_groseria:
            return {"message": "El texto tiene grosería(s)", "tieneGroseria": True, "status": 200},
        
        print("guardando")
        print(chat["username"])
        
        try:     
            new_chat = Model(
                IdChat=chat['IdChat'],
                IdUser=chat['IdUser'],
                date=chat['date'],
                hour=chat['hour'],
                text=chat['text'],
                username=chat["username"]
            )       
            self.db.add(new_chat)
            self.db.commit()
            return {"message": "El texto está limpio", "tieneGroseria": False, "status": 200},
        
        except Exception as e:
            print("Error al guardar en la base de datos:", str(e))
            self.db.rollback()  # Revertir cambios en caso de error
            return {"message": str(e), "status": "error"},

    def list(self):
        try:
            chats = self.db.query(Model).all()
            value = [{
                "IdChat": item.IdChat,
                "IdUser": item.IdUser,
                "date": str(item.date),
                "hour": str(item.hour),
                "text": item.text,
                "username": item.username,
            } for item in chats]
            
            self.db.commit()
            return {
                "error": False,
                "status": 200,
                "message": f"Se encontraron {len(value)} citas médicas",
                "value": value,
            }
        
        except Exception as e:
            print("Error al listar los chats:", str(e))
            return {"message": str(e), "status": "error"},
