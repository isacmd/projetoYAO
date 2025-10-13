from abc import ABC, abstractmethod
from typing import List

# template method para processar documentos
class ProcessadorDocumento(ABC):
    
    # template method - define esqueleto do algoritmo
    def processar(self, arquivo: str) -> str:
        print(f"\n{'='*60}")
        print(f"processando documento: {arquivo}")
        print(f"{'='*60}")
        
        # passos do algoritmo (alguns fixos, outros variáveis)
        self._validar_arquivo(arquivo)
        conteudo = self._ler_arquivo(arquivo)
        dados = self._extrair_dados(conteudo)
        dados_processados = self._processar_dados(dados)
        resultado = self._formatar_saida(dados_processados)
        self._salvar_resultado(resultado)
        
        print("processamento concluído!")
        return resultado
    
    # passo fixo - valida se arquivo existe
    def _validar_arquivo(self, arquivo: str) -> None:
        print("1. validando arquivo...")
        if not arquivo.endswith(self._get_extensao()):
            raise ValueError(f"arquivo deve ser {self._get_extensao()}")
        print("   arquivo válido")
    
    # passo fixo - lê conteúdo do arquivo
    def _ler_arquivo(self, arquivo: str) -> str:
        print("2. lendo arquivo...")
        # simulação
        conteudo = f"conteúdo do arquivo {arquivo}"
        print(f"   {len(conteudo)} caracteres lidos")
        return conteudo
    
    @abstractmethod
    # passo variável - subclasse implementa
    def _extrair_dados(self, conteudo: str) -> List:
        pass
    
    @abstractmethod
    # passo variável - subclasse implementa
    def _processar_dados(self, dados: List) -> List:
        pass
    
    # hook method - pode ser sobrescrito
    def _formatar_saida(self, dados: List) -> str:
        print("5. formatando saída (padrão)...")
        return str(dados)
    
    # passo fixo - salva resultado
    def _salvar_resultado(self, resultado: str) -> None:
        print("6. salvando resultado...")
        print(f"   resultado: {resultado[:50]}...")
    
    @abstractmethod
    # retorna extensão do arquivo
    def _get_extensao(self) -> str:
        pass