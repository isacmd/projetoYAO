from typing import Dict, List
from .prototype import Prototype

# registro de protótipos para clonagem
class PrototypeRegistry:
    
    def __init__(self):
        self._prototipos: Dict[str, Prototype] = {}
    
    # registra um protótipo
    def registrar(self, nome: str, prototipo: Prototype) -> None:
        self._prototipos[nome] = prototipo
        print(f"protótipo '{nome}' registrado: {prototipo}")
    
    # cria clone de um protótipo registrado
    def criar(self, nome: str) -> Prototype:
        if nome not in self._prototipos:
            raise ValueError(f"protótipo '{nome}' não encontrado")
        
        clone = self._prototipos[nome].clone()
        print(f"clone criado a partir de '{nome}': {clone}")
        return clone
    
    # lista protótipos registrados
    def listar(self) -> List[str]:
        return list(self._prototipos.keys())