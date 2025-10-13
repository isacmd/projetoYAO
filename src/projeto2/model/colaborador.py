from typing import List
from datetime import datetime
from .component import ComponenteCadastro

class Colaborador(ComponenteCadastro):
    """classe composite que agrega todas as seções do cadastro"""
    
    def __init__(self, id: str, nome: str):
        self._id = id
        self._nome = nome
        self._secoes: List[ComponenteCadastro] = []
        self._data_criacao = datetime.now()
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nome(self) -> str:
        return self._nome
    
    def adicionar(self, componente: ComponenteCadastro) -> None:
        self._secoes.append(componente)
    
    def remover(self, componente: ComponenteCadastro) -> None:
        self._secoes.remove(componente)
    
    def obter_filhos(self) -> List[ComponenteCadastro]:
        return self._secoes
    
    def exibir(self, nivel: int = 0) -> str:
        indent = "  " * nivel
        resultado = f"{indent}┌─ COLABORADOR: {self._nome} (ID: {self._id})\n"
        
        for i, secao in enumerate(self._secoes):
            is_last = (i == len(self._secoes) - 1)
            prefix = "└─" if is_last else "├─"
            resultado += f"{indent}{prefix} {secao.exibir(nivel + 1)}\n"
        
        return resultado
    
    def to_dict(self) -> dict:
        """serializa colaborador para dicionário"""
        return {
            'id': self._id,
            'nome': self._nome,
            'data_criacao': self._data_criacao.isoformat(),
            'secoes': [type(s).__name__ for s in self._secoes]
        }