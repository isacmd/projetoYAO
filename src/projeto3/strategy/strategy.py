from abc import ABC, abstractmethod
from typing import List

# interface strategy
class Strategy(ABC):
    
    @abstractmethod
    # executa algoritmo específico
    def executar(self, dados: List[int]) -> List[int]:
        pass
    
    @abstractmethod
    # retorna nome da estratégia
    def get_nome(self) -> str:
        pass
