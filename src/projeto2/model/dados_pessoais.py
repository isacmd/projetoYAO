from typing import List, Optional
from .component import ComponenteCadastro

class DadosPessoais(ComponenteCadastro):
    
    def __init__(self, nome: str, cpf: str, rg: Optional[str] = None):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dependentes: List[str] = []
        self.contatos: List[str] = []
    
    def adicionar_dependente(self, nome: str) -> None:
        self.dependentes.append(nome)
    
    def adicionar_contato(self, contato: str) -> None:
        self.contatos.append(contato)
    
    def exibir(self, nivel: int = 0) -> str:
        info = f"DADOS PESSOAIS\n"
        indent = "  " * (nivel + 1)
        info += f"{indent}Nome: {self.nome}\n"
        info += f"{indent}CPF: {self.cpf}\n"
        if self.rg:
            info += f"{indent}RG: {self.rg}\n"
        if self.dependentes:
            info += f"{indent}Dependentes: {', '.join(self.dependentes)}\n"
        if self.contatos:
            info += f"{indent}Contatos: {', '.join(self.contatos)}"
        return info.rstrip()