from src.api.Domain.Ports.ChatPort import ChatPort as Port
from src.api.Domain.Entity.Chat import Chat


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):     
        # print("controller create",data)   
        try:
            return self.repository.save(data)
        except Exception as e:
            return {"error": str(e), "status": "Unexpected data","m":"s"}, 500
