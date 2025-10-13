from enum import Enum
from .component import ComponenteCadastro

class TipoDocumento(Enum):
    RG = "RG"
    CPF = "CPF"
    CTPS = "CTPS"
    CNH = "CNH"
    TITULO_ELEITOR = "Título de Eleitor"
    CERTIFICADO_RESERVISTA = "Certificado de Reservista"

class Documento(ComponenteCadastro):
    
    def __init__(self, tipo: TipoDocumento, numero: str):
        self.tipo = tipo
        self.numero = numero
        self.orgao_emissor: str = ""
        self.data_emissao: str = ""
    
    def exibir(self, nivel: int = 0) -> str:
        indent = "  " * (nivel + 1)
        info = f"DOCUMENTO: {self.tipo.value}\n"
        info += f"{indent}Número: {self.numero}"
        if self.orgao_emissor:
            info += f"\n{indent}Órgão: {self.orgao_emissor}"
        if self.data_emissao:
            info += f"\n{indent}Emissão: {self.data_emissao}"
        return info