from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional
from datetime import datetime

T = TypeVar('T')

# interface genérica para data access objects
class BaseDAO(ABC, Generic[T]):
  
    # insere uma nova entidade
    @abstractmethod
    def inserir(self, entidade: T) -> None:
        pass
    
    # atualiza entidade existente
    @abstractmethod
    def atualizar(self, entidade: T) -> None:
        pass
    
    # remove entidade por ID
    @abstractmethod
    def deletar(self, id: str) -> bool:
        pass
    
    # busca entidade por ID
    @abstractmethod
    def buscar_por_id(self, id: str) -> Optional[T]:
        pass
    
    # retorna todas as entidades
    @abstractmethod
    def buscar_todos(self) -> List[T]:
        pass
    
    # registra operação no log
    def registrar_log(self, operacao: str, id: str) -> None:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[LOG] {operacao} - ID: {id} - {timestamp}")