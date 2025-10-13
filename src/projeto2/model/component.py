from abc import ABC, abstractmethod
from typing import List

class ComponenteCadastro(ABC):
    """componente base para padrão composite"""
    
    @abstractmethod
    def exibir(self, nivel: int = 0) -> str:
        pass
    
    def adicionar(self, componente: 'ComponenteCadastro') -> None:
        raise NotImplementedError("Operação não suportada")
    
    def remover(self, componente: 'ComponenteCadastro') -> None:
        raise NotImplementedError("Operação não suportada")
    
    def obter_filhos(self) -> List['ComponenteCadastro']:
        return []