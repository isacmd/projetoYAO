from typing import List, Dict
from datetime import datetime
import copy
from .prototype import Prototype

# prototype concreto - documento
class Documento(Prototype):
    
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo
        self.data_criacao = datetime.now()
        self.tags: List[str] = []
        self.metadados: Dict = {}
    
    # clone profundo
    def clone(self) -> 'Documento':
        novo = copy.deepcopy(self)
        novo.data_criacao = datetime.now()  # atualiza data
        return novo
    
    def adicionar_tag(self, tag: str) -> None:
        self.tags.append(tag)
    
    def __str__(self) -> str:
        return f"Documento('{self.titulo}', criado em {self.data_criacao.strftime('%H:%M:%S')})"

# prototype concreto - configuração
class Configuracao(Prototype):
    
    def __init__(self, nome: str):
        self.nome = nome
        self.parametros: Dict[str, any] = {}
        self.habilitado = True
    
    # clone profundo
    def clone(self) -> 'Configuracao':
        return copy.deepcopy(self)
    
    def definir(self, chave: str, valor: any) -> None:
        self.parametros[chave] = valor
    
    def __str__(self) -> str:
        status = "habilitado" if self.habilitado else "desabilitado"
        return f"Config('{self.nome}' [{status}], {len(self.parametros)} params)"

# prototype concreto - perfil de usuário
class PerfilUsuario(Prototype):
    
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo  # "admin", "usuario", "convidado"
        self.permissoes: List[str] = []
        self.preferencias: Dict = {
            "tema": "claro",
            "idioma": "pt-BR",
            "notificacoes": True
        }
    
    # clone profundo
    def clone(self) -> 'PerfilUsuario':
        return copy.deepcopy(self)
    
    def adicionar_permissao(self, permissao: str) -> None:
        if permissao not in self.permissoes:
            self.permissoes.append(permissao)
    
    def __str__(self) -> str:
        return f"Perfil('{self.nome}' [{self.tipo}], {len(self.permissoes)} permissões)"
