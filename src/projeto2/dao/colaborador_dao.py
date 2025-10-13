from typing import Dict, List, Optional
from ..model.colaborador import Colaborador
from .base_dao import BaseDAO

# DAO para colaborador com singleton
class ColaboradorDAO(BaseDAO[Colaborador]):
    
    _instance: Optional['ColaboradorDAO'] = None
    
    def __new__(cls) -> 'ColaboradorDAO':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._database = {}
        return cls._instance
    
    # inicializa database se necessário
    def __init__(self):
        if not hasattr(self, '_database'):
            self._database: Dict[str, Colaborador] = {}
    
    # insere novo colaborador
    def inserir(self, colaborador: Colaborador) -> None: 
        if colaborador.id in self._database:
            raise ValueError(f"Colaborador com ID {colaborador.id} já existe")
        
        self._database[colaborador.id] = colaborador
        self.registrar_log("INSERT", colaborador.id)
    
    # atualiza colaborador existente
    def atualizar(self, colaborador: Colaborador) -> None:
        if colaborador.id not in self._database:
            raise ValueError(f"Colaborador com ID {colaborador.id} não encontrado")
        
        self._database[colaborador.id] = colaborador
        self.registrar_log("UPDATE", colaborador.id)
    
    # remove colaborador por id
    def deletar(self, id: str) -> bool:
        if id in self._database:
            del self._database[id]
            self.registrar_log("DELETE", id)
            return True
        return False
    
    # busca colaborador por id
    def buscar_por_id(self, id: str) -> Optional[Colaborador]:
        return self._database.get(id)
    
    # retorna todos os colaboradores
    def buscar_todos(self) -> List[Colaborador]:
        return list(self._database.values())
    
    # busca colaboradores por nome 
    def buscar_por_nome(self, nome: str) -> List[Colaborador]:
        return [c for c in self._database.values() 
                if nome.lower() in c.nome.lower()]
    
    # limpa todos os registros 
    def limpar(self) -> None:
        self._database.clear()
        print("[LOG] Database limpo")