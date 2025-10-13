from abc import ABC, abstractmethod
from typing import List
from ..model.colaborador import Colaborador

# template method para geração de relatórios
class TemplateRelatorio(ABC):
    
    # template method - define esqueleto do algoritmo
    def gerar(self, colaboradores: List[Colaborador]) -> str:
        relatorio = self._criar_cabecalho()
        relatorio += self._criar_corpo(colaboradores)
        relatorio += self._criar_rodape(colaboradores)
        return relatorio
    
    @abstractmethod
    def _criar_cabecalho(self) -> str:
        pass
    
    @abstractmethod
    def _criar_corpo(self, colaboradores: List[Colaborador]) -> str:
        pass
    
    # hook method - pode ser sobrescrito
    def _criar_rodape(self, colaboradores: List[Colaborador]) -> str:
        return f"\n{'='*60}\nTotal de colaboradores: {len(colaboradores)}\n"

# relatório em formato html
class RelatorioHTML(TemplateRelatorio):
    
    def _criar_cabecalho(self) -> str:
        return """
<!DOCTYPE html>
<html>
<head>
    <title>Relatório de Colaboradores</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
    </style>
</head>
<body>
    <h1>Relatório de Colaboradores</h1>
    <table>
        <tr><th>ID</th><th>Nome</th><th>Data Criação</th></tr>
"""
    
    def _criar_corpo(self, colaboradores: List[Colaborador]) -> str:
        corpo = ""
        for colab in colaboradores:
            dados = colab.to_dict()
            corpo += f"        <tr><td>{dados['id']}</td><td>{dados['nome']}</td><td>{dados['data_criacao']}</td></tr>\n"
        return corpo
    
    def _criar_rodape(self, colaboradores: List[Colaborador]) -> str:
        return f"""
    </table>
    <p><strong>Total: {len(colaboradores)} colaboradores</strong></p>
</body>
</html>
"""

# relatório em formato texto simples (simula pdf)
class RelatorioPDF(TemplateRelatorio):
    
    def _criar_cabecalho(self) -> str:
        return """
════════════════════════════════════════════════════════════
             RELATÓRIO DE COLABORADORES - PDF               
════════════════════════════════════════════════════════════

"""
    
    def _criar_corpo(self, colaboradores: List[Colaborador]) -> str:
        corpo = ""
        for colab in colaboradores:
            dados = colab.to_dict()
            corpo += f"\n┌─ ID: {dados['id']}\n"
            corpo += f"│  Nome: {dados['nome']}\n"
            corpo += f"│  Criado em: {dados['data_criacao'][:10]}\n"
            corpo += f"└─ Seções: {', '.join(dados['secoes'])}\n"
        return corpo

# relatório em formato csv
class RelatorioCSV(TemplateRelatorio):
    
    def _criar_cabecalho(self) -> str:
        return "ID,Nome,Data_Criacao,Secoes\n"
    
    def _criar_corpo(self, colaboradores: List[Colaborador]) -> str:
        corpo = ""
        for colab in colaboradores:
            dados = colab.to_dict()
            secoes = ';'.join(dados['secoes'])
            corpo += f"{dados['id']},{dados['nome']},{dados['data_criacao']},{secoes}\n"
        return corpo
    
    def _criar_rodape(self, colaboradores: List[Colaborador]) -> str:
        return f"\n# Total de registros: {len(colaboradores)}\n"

# factory method para criar diferentes tipos de relatórios
class RelatorioFactory:
    
    @staticmethod
    # factory method
    def criar_relatorio(tipo: str) -> TemplateRelatorio:
        tipos_validos = {
            'html': RelatorioHTML,
            'pdf': RelatorioPDF,
            'csv': RelatorioCSV
        }
        
        tipo_lower = tipo.lower()
        if tipo_lower not in tipos_validos:
            raise ValueError(f"Tipo '{tipo}' inválido. Use: {', '.join(tipos_validos.keys())}")
        
        return tipos_validos[tipo_lower]()