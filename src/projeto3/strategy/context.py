import time
from typing import List
from .strategy import Strategy

# context que usa strategy
class ContextoOrdenacao:
    
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy
    
    # define estratégia de ordenação
    def definir_estrategia(self, strategy: Strategy) -> None:
        self._strategy = strategy
        print(f"estratégia definida: {strategy.get_nome()}")
    
    # ordena dados usando estratégia atual
    def ordenar(self, dados: List[int]) -> List[int]:
        if not self._strategy:
            raise ValueError("nenhuma estratégia definida")
        
        print(f"\nordenando com {self._strategy.get_nome()}...")
        print(f"    dados originais: {dados}")
        
        inicio = time.time()
        resultado = self._strategy.executar(dados)
        tempo = (time.time() - inicio) * 1000
        
        print(f"    dados ordenados: {resultado}")
        print(f"    tempo: {tempo:.4f}ms")
        
        return resultado
    
    # compara performance de diferentes estratégias
    def comparar_estrategias(self, dados: List[int], estrategias: List[Strategy]) -> None:
        print("\n" + "="*60)
        print("COMPARAÇÃO DE ESTRATÉGIAS")
        print("="*60)
        print(f"tamanho dos dados: {len(dados)} elementos")
        print(f"estratégias: {len(estrategias)}\n")
        
        resultados = []
        for estrategia in estrategias:
            self.definir_estrategia(estrategia)
            inicio = time.time()
            self._strategy.executar(dados)
            tempo = (time.time() - inicio) * 1000
            resultados.append((estrategia.get_nome(), tempo))
            print(f"  {estrategia.get_nome()}: {tempo:.4f}ms")
        
        print("\nMais rápido: " + min(resultados, key=lambda x: x[1])[0])
