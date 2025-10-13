from datetime import date
from decimal import Decimal
from .component import ComponenteCadastro

class DadosAdmissionais(ComponenteCadastro):
    
    def __init__(self, cargo: str, data_admissao: date, salario: Decimal):
        self.cargo = cargo
        self.data_admissao = data_admissao
        self.salario = salario
        self.setor: str = ""
        self.gestor: str = ""
    
    def exibir(self, nivel: int = 0) -> str:
        indent = "  " * (nivel + 1)
        info = f"DADOS ADMISSIONAIS\n"
        info += f"{indent}Cargo: {self.cargo}\n"
        info += f"{indent}Admissão: {self.data_admissao.strftime('%d/%m/%Y')}\n"
        info += f"{indent}Salário: R$ {self.salario:,.2f}"
        if self.setor:
            info += f"\n{indent}Setor: {self.setor}"
        if self.gestor:
            info += f"\n{indent}Gestor: {self.gestor}"
        return info