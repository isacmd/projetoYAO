from typing import Protocol
from ..model.colaborador import Colaborador
from ..model.dados_pessoais import DadosPessoais

# sistema legado com interface incompatível
class SistemaLegadoValidacao:
  
    # método legado que retorna tupla
    def validar_cpf_antigo(self, numero: str) -> tuple[bool, str]:
        # validação simples de CPF
        cpf = ''.join(filter(str.isdigit, numero))
        if len(cpf) != 11:
            return (False, "CPF deve ter 11 dígitos")
        return (True, "CPF válido")
    
    # retorna lista de campos faltantes
    def verificar_dados_completos(self, dados: dict) -> list:
        campos_obrigatorios = ['nome', 'cpf']
        return [c for c in campos_obrigatorios if c not in dados or not dados[c]]

# adapter que adapta interface legada para interface
class ValidadorAdapter:
    
    def __init__(self):
        self._sistema_legado = SistemaLegadoValidacao()
    
    def validar(self, colaborador: Colaborador) -> None:
        # busca dados pessoais nas seções
        dados_pessoais = None
        for secao in colaborador.obter_filhos():
            if isinstance(secao, DadosPessoais):
                dados_pessoais = secao
                break
        
        if not dados_pessoais:
            raise ValueError("Colaborador deve ter dados pessoais")
        
        # adapta validação de CPF
        valido, mensagem = self._sistema_legado.validar_cpf_antigo(dados_pessoais.cpf)
        if not valido:
            raise ValueError(mensagem)
        
        # adapta verificação de campos obrigatórios
        dados_dict = {
            'nome': dados_pessoais.nome,
            'cpf': dados_pessoais.cpf
        }
        campos_faltantes = self._sistema_legado.verificar_dados_completos(dados_dict)
        if campos_faltantes:
            raise ValueError(f"Campos obrigatórios faltando: {', '.join(campos_faltantes)}")