from abc import ABC, abstractmethod
from typing import List

# interface command
class Command(ABC):
    
    # executa o comando
    @abstractmethod
    def execute(self) -> str:
        pass
    
    # desfaz o comando
    @abstractmethod
    def undo(self) -> str:
        pass
    
    # retorna nome do comando
    @abstractmethod
    def get_name(self) -> str:
        pass