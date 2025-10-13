from enum import Enum
from .component import ComponenteCadastro

class TipoEndereco(Enum):
    RESIDENCIAL = "residencial"
    COMERCIAL = "comercial"

class Endereco(ComponenteCadastro):
    
    def __init__(self, tipo: TipoEndereco, logradouro: str, 
                 cidade: str, estado: str, cep: str):
        self.tipo = tipo
        self.logradouro = logradouro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.numero: str = ""
        self.complemento: str = ""
    
    def exibir(self, nivel: int = 0) -> str:
        indent = "  " * (nivel + 1)
        info = f"ENDEREÇO {self.tipo.value.upper()}\n"
        info += f"{indent}{self.logradouro}"
        if self.numero:
            info += f", {self.numero}"
        if self.complemento:
            info += f" - {self.complemento}"
        info += f"\n{indent}{self.cidade}/{self.estado}\n"
        info += f"{indent}CEP: {self.cep}"
        return info