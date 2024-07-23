from abc import ABC, abstractmethod
from src.api.Domain.Entity.Chat import Chat


class ChatPort(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def save(self, chat):
        pass

    @abstractmethod
    def list(self):
        pass
