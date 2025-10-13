from abc import ABC, abstractmethod
from typing import List

# interface observer
class Observer(ABC):
    
    @abstractmethod
    # recebe notificação do subject
    def atualizar(self, mensagem: str) -> None:
        pass

# interface subject
class Subject(ABC):
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    # adiciona observer
    def anexar(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer {type(observer).__name__} anexado")
    
    # remove observer
    def desanexar(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer {type(observer).__name__} desanexado")
    
    # notifica todos os observers
    def notificar(self, mensagem: str) -> None:
        print(f"\nNotificando {len(self._observers)} observer(s)...")
        for observer in self._observers:
            observer.atualizar(mensagem)
