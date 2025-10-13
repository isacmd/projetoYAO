from typing import List
from .template_method import ProcessadorDocumento

# processa arquivos csv
class ProcessadorCSV(ProcessadorDocumento):
    
    def _extrair_dados(self, conteudo: str) -> List:
        print("3. extraindo dados do csv...")
        # simulação
        dados = [["col1", "col2"], ["val1", "val2"]]
        print(f"   {len(dados)} linhas extraídas")
        return dados
    
    def _processar_dados(self, dados: List) -> List:
        print("4. processando dados do csv...")
        # simulação - converte para dicionários
        headers = dados[0]
        resultado = [dict(zip(headers, row)) for row in dados[1:]]
        print(f"   {len(resultado)} registros processados")
        return resultado
    
    def _get_extensao(self) -> str:
        return ".csv"

# processa arquivos json
class ProcessadorJSON(ProcessadorDocumento):
    
    def _extrair_dados(self, conteudo: str) -> List:
        print("3. extraindo dados do json...")
        # simulação
        dados = {"key": "value", "items": [1, 2, 3]}
        print(f"   estrutura json extraída")
        return [dados]
    
    def _processar_dados(self, dados: List) -> List:
        print("4. processando dados do json...")
        # simulação - valida estrutura
        resultado = [f"{k}: {v}" for item in dados for k, v in item.items()]
        print(f"   {len(resultado)} campos processados")
        return resultado
    
    # sobrescreve formatação para json
    def _formatar_saida(self, dados: List) -> str:
        print("5. formatando saída (json)...")
        import json
        return json.dumps({"resultado": dados}, indent=2)
    
    def _get_extensao(self) -> str:
        return ".json"

# processa arquivos xml
class ProcessadorXML(ProcessadorDocumento):
    
    def _extrair_dados(self, conteudo: str) -> List:
        print("3. extraindo dados do xml...")
        # simulação
        dados = [("<tag>", "valor")]
        print(f"   {len(dados)} elementos xml extraídos")
        return dados
    
    def _processar_dados(self, dados: List) -> List:
        print("4. processando dados do xml...")
        # simulação - converte tags
        resultado = [f"{tag} = {val}" for tag, val in dados]
        print(f"   {len(resultado)} elementos processados")
        return resultado
    
    def _get_extensao(self) -> str:
        return ".xml"
