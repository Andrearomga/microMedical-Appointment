from src.api.Domain.Ports.ChatPort import ChatPort as Port

class ListAll:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):        
        try:
            return self.repository.list()
        except Exception as e:
            return {"error": str(e), "status": "Unexpected error"}, 500
